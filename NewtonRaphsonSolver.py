from tkinter import *
from mpmath import mp
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
root = Tk()



def solve():
    x = Symbol('x')
    resVar.set("")
    try:
        if(funcVar.get() == "" or ipVar.get() == ""):
            resVar.set("please Input Func and Init point")
            return
        if(noiVar.get() == ""):
            noiVar.set("20")
        if(errVar.get() == ""):
            errVar.set(0.0001)
        try:
            x0 = float(ipVar.get())
        except ValueError:
            print("Input correct value for initial Point")

        transformation = (standard_transformations + (implicit_multiplication_application, ))


        fx = parse_expr(funcVar.get(),transformations=transformation)
        print(fx)
        f = lambdify(x,fx)
        dfx = diff(fx)
        print(dfx)
        df = lambdify(x, dfx)
        i = 1
        while  i < int(noiVar.get()):

            x1 = x0 - f(x0)/df(x0)
            er = abs((x1-x0)/x1)

            print (i, x1,er)
            if(abs((x1-x0)/x1) < float(errVar.get())):
                resVar.set("root is {:.6f}, No. of ittr is {}".format(x1,i))

                return
            elif f(x1) == 0 :
                resVar.set(f"root : {x1} and Itteration : {i}")
                return

            x0 = x1

            i+=1
        resVar.set("not converging")
    except ValueError :
        resVar.set("VE:please input correct values")
    except ZeroDivisionError:
        resVar.set("Zero division error")
    except TypeError:
        resVar.set("TE:please input correct values")
    # print(ipVar.get())
    # print(noiVar.get())
    # print(errVar.get())
    # ipVar.set(1.2)
    # resVar.set("haha")


root.title("Newton Raphson Solver")
root.resizable(0,0)
root.image = PhotoImage(file="77.gif")
w = root.image.width()
h = root.image.height()
root.configure(background='wheat')
# background_label = Label(root, image=root.image)

# background_label.pack(side='top',fill = BOTH,expand = 'yes')

root.geometry( "%dx%d+100+100" % (w,h))


frameOne = Frame(root,bg = 'wheat')
frameOne.pack(side = TOP, fill = X)
frameTwo = Frame(root,bg = 'wheat')
frameTwo.pack(side = TOP, fill = X)
frameThree = Frame(root,bg ='wheat')
frameThree.pack(side = TOP, fill = X)
frameFour = Frame(root,bg ='wheat')
frameFour.pack(side = TOP, fill = X)
frameFive = Frame(root,bg = 'wheat')
frameFive.pack(side = TOP, fill = X)
frameSix = Frame(root,bg = 'wheat')
frameSix.pack(side = BOTTOM, fill = X)

funcVar = StringVar(frameOne, value='x**3-2x*2')
func = Label(frameOne, text = "Input function",bg = 'wheat')
func.configure(font=("Helvetica", 18))
func.pack(padx=16,pady=16,side=LEFT)
funcEntry = Entry(frameOne,font = "Helvetica 18",textvariable=funcVar).pack(padx=80,pady=16,side=LEFT)

ipVar = StringVar(frameTwo, value='1.5')
ipLabel = Label(frameTwo, text = "Initial Point",bg = 'wheat')
ipLabel.configure(font=("Helvetica", 18))
ipLabel.pack(padx=16, pady=16, side=LEFT)
ipEntry = Entry(frameTwo,font = "Helvetica 18",width = 8,textvariable=ipVar).pack(padx=110  ,pady=16,side=LEFT)

noiVar = StringVar(root, value='20')
noiLable = Label(frameThree, text = "No of Itteration",bg = 'wheat')
noiLable.configure(font=("Helvetica", 18))
noiLable.pack(padx=16,pady=16,side=LEFT)
noiEntry = Entry(frameThree,font = "Helvetica 18",width = 8,textvariable=noiVar).pack(padx=70,pady=16,side=LEFT)

errVar = StringVar(root, value='0.0001')
errLable = Label(frameFour, text = "Error up to sign. digit",bg = 'wheat')
errLable.configure(font=("Helvetica", 18))
errLable.pack(padx=16,pady=16,side=LEFT)
errEntry = Entry(frameFour,font = "Helvetica 18",width = 8,textvariable=errVar).pack(padx=0,pady=16,side=LEFT)

resVar = StringVar(frameFive,value="")
res = Label(frameFive, text = "Result : ",bg = 'wheat')
res.configure(font=("Helvetica", 18))
res.pack(padx=16,pady=16,side=LEFT)
result = Label(frameFive, textvariable=resVar,bg = 'wheat')
result.configure(font=("Helvetica", 14))
result.pack(padx=0,pady=16,side=LEFT)

SolveButton = Button(frameSix,font = "Helvetica 18",text = "solve!",bg = "white",height=5, width=40,command = solve).pack(padx=10,pady=10,side=BOTTOM)




root.mainloop();