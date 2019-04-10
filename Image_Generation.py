from core import G
import humanmodifier

class extract:

    def __init__(self):

        import pandas as pd
        self.df = pd.read_csv('table1.csv')  #reading the database file in csv format

    def debug(self):

            print(self.df.shape)

    def image_generate(self):
        
        human = G.app.mhapi.modifiers.human
        Measurerer = (__import__("0_modeling_a_measurement"))
        ruler = Measurerer.Ruler() 
        #print 'waist [cm]: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')
        ###macro_modifiers###
        human.setAgeYears(25)
        human.setWeight(1.0)
        human.setHeight(0.5)
        human.setMuscle(1.0)
        human.setGender(1.0)
        human.setBodyProportions(1.0)
        ###macro_end###

        for i in range(2):
            ##measure modifiers##Currently arbitrary values are set but any value can be set between 0.0 to 1.0
            human.getModifier('measure/measure-neck-circ-decr|incr').setValue(self.df.iloc[i][4]) #set neck circumference for human model
            human.getModifier('measure/measure-neck-height-decr|incr').setValue(self.df.iloc[i][5]) #set neck height for human model
            human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(self.df.iloc[i][6]) #set upper arm circumference for human model
            human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(self.df.iloc[i][7]) #set upper arm length for human model
            human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(self.df.iloc[i][8]) #set lower arm length for human model
            human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(self.df.iloc[i][9]) #set wrist circumference for human model
            human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(self.df.iloc[i][10]) #set front chest distance for human model
            human.getModifier('measure/measure-bust-circ-decr|incr').setValue(self.df.iloc[i][11]) #set bust circumference for human model
            human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(self.df.iloc[i][12]) #set underbust  circumference for human model
            human.getModifier('measure/measure-waist-circ-decr|incr').setValue(self.df.iloc[i][13]) #set waist circumference for human model
            human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(self.df.iloc[i][14]) #set nape to waist distance for human model
            human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(self.df.iloc[i][15]) #set waist to hip for human model
            human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(self.df.iloc[i][16]) #set shoulder distance for human model
            human.getModifier('measure/measure-hips-circ-decr|incr').setValue(self.df.iloc[i][17]) #set hip circumference for human model
            human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(self.df.iloc[i][18]) #set upper leg height for human model
            human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(self.df.iloc[i][19]) #set thigh circumference for human model
            human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(self.df.iloc[i][20]) #set lower leg height for human model
            human.getModifier('measure/measure-calf-circ-decr|incr').setValue(self.df.iloc[i][21]) #set calf circumference for human model
            human.getModifier('measure/measure-knee-circ-decr|incr').setValue(self.df.iloc[i][22]) #set knee circumference for human model
            human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(self.df.iloc[i][23]) #set ankle circumference for human model
            ##measure modifiers_ends##

            human.applyAllTargets() #This is to apply the above value changes to the model  
            #print 'waist [cm], 1.0: ',ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric')

            ##print( "waist [cm], -1.0: ",ruler.getMeasure(human,'measure/measure-waist-circ-decr|incr','metric'))   print syntax when using Python3 Makehuman package.

            MHScript.screenShot('/home/hk/Desktop/front%d.png'%(i)) #takes screenshot and save to grab folder

            MHScript.modifyRotationZ(-90.0) #rotate to take screenshot in side view

            MHScript.screenShot('/home/hk/Desktop/side%d.png'%(i))

            MHScript.modifyRotationZ(90.0) #rotate to return back to front view

o = extract()
o.image_generate()
