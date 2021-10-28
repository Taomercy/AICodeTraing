import matplotlib.pylab as plt
import sympy
from numpy import array, arange

data = array([
    [1.2, 3.6],
    [2.3, 4.6],
    [1.8, 7.6],
    [5.4, 15.8],
    [6.2, 20.9],
    [7.5, 12.7],
])


class Curve(object):
    formula = None
    module = "dynamic_equation"
    filename = module + ".py"

    def __init__(self, n):
        if n <= 0:
            print("Error: n should >= 0")
            return
        # generate curve function
        self.formula = "a0*x**{}".format(n)
        for i in range(1, n):
            self.formula += "+a{0}*x**{1}".format(i, n-i)
        self.formula += "+a{0}".format(n)

        parameters = ["a{}".format(i) for i in range(0, n+1)]
        parameter_list = "(x, " + ", ".join(parameters) + ")"
        p_code = ", ".join(parameters)

        with open(self.filename, "w") as fw:
            code = "import matplotlib.pylab as plt\n"
            code += "import sympy\n"
            code += "from numpy import array, arange\n\n\n"
            code += """def curve{0}:\n\treturn {1}\n\n\n""".format(parameter_list, self.formula)
            fw.write(code)

            # generate resolver
            code = "def resolver(data):\n"
            code += "\t{0} = sympy.symbols('{1}')\n".format(p_code, " ".join(parameters))
            code += "\tdef plotting(paras, data):\n"
            code += "\t\tfig = plt.figure()\n"
            code += "\t\tax = fig.add_subplot(111)\n"
            code += "\t\tax.scatter(array(data[:, 0]), array(data[:, 1]))\n"
            code += "\t\tmax_number = data[:, 0].max()\n"
            code += "\t\tmin_number = data[:, 0].min()\n"
            code += "\t\tstep = (max_number-min_number)/1000\n"
            code += "\t\tx = arange(min_number*0.1, max_number*1.1, step)\n"
            paras = ["paras[{}]".format(i) for i in parameters]
            code += "\t\ty = curve(x, {})\n".format(", ".join(paras))
            code += "\t\tax.plot(x, y, 'r')\n"
            code += "\t\tplt.show()\n"
            code += "\tloss = sympy.Symbol('loss')\n"
            code += "\tfor i in data:\n"
            code += "\t\tloss += (i[1] - curve(i[0], {})) ** 2\n".format(p_code)
            code += "\n".join(["\tdlossd{0} = sympy.diff(loss, {0})".format(p) for p in parameters])
            code += "\n\tres = sympy.solve([{}], [{}])\n".format(", ".join(["dlossd{0}".format(p) for p in parameters]), p_code)
            code += "\n\tprint(\"formula = {}\")\n".format(self.formula)
            code += "\n".join(["\tprint(\"{0} =\", res[{0}])".format(p) for p in parameters])
            code += "\n\tplotting(res, data)\n"
            fw.write(code)

    def run(self, data):
        module = __import__(self.module)
        func = getattr(module, "resolver")
        func(data)


if __name__ == '__main__':
    c = Curve(2)
    c.run(data)
