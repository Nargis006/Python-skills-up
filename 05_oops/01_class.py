class Tea:
    type= "Masala_Chai"

cutting = Tea()
cutting.type = "LemonTea"
cutting.customize = False
cutting.milk="Mild"


# when we create properties at object level and if the same property exist in class level shadowing will happen and on print object.type object value will be displayed. when we delete object type on call of object.type it will call class peroperty and will throw error if class doesnot have that pproperty in it.

del cutting.milk
print(cutting.type)
#print(cutting.milk) # will throw error as it can't fall back to class property as it does'nt have that.