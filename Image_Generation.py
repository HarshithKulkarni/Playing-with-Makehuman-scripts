from core import G
import humanmodifier





class extract:

    def __init__(self):

        import pandas as pd
        self.df = pd.read_csv('table1.csv')

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
            human.getModifier('measure/measure-neck-circ-decr|incr').setValue(self.df.iloc[i][4])
            human.getModifier('measure/measure-neck-height-decr|incr').setValue(self.df.iloc[i][5])
            human.getModifier('measure/measure-upperarm-circ-decr|incr').setValue(self.df.iloc[i][6])
            human.getModifier('measure/measure-upperarm-length-decr|incr').setValue(self.df.iloc[i][7])
            human.getModifier('measure/measure-lowerarm-length-decr|incr').setValue(self.df.iloc[i][8])
            human.getModifier('measure/measure-wrist-circ-decr|incr').setValue(self.df.iloc[i][9])
            human.getModifier('measure/measure-frontchest-dist-decr|incr').setValue(self.df.iloc[i][10])
            human.getModifier('measure/measure-bust-circ-decr|incr').setValue(self.df.iloc[i][11])
            human.getModifier('measure/measure-underbust-circ-decr|incr').setValue(self.df.iloc[i][12])
            human.getModifier('measure/measure-waist-circ-decr|incr').setValue(self.df.iloc[i][13])
            human.getModifier('measure/measure-napetowaist-dist-decr|incr').setValue(self.df.iloc[i][14])
            human.getModifier('measure/measure-waisttohip-dist-decr|incr').setValue(self.df.iloc[i][15])
            human.getModifier('measure/measure-shoulder-dist-decr|incr').setValue(self.df.iloc[i][16])
            human.getModifier('measure/measure-hips-circ-decr|incr').setValue(self.df.iloc[i][17])
            human.getModifier('measure/measure-upperleg-height-decr|incr').setValue(self.df.iloc[i][18])
            human.getModifier('measure/measure-thigh-circ-decr|incr').setValue(self.df.iloc[i][19])
            human.getModifier('measure/measure-lowerleg-height-decr|incr').setValue(self.df.iloc[i][20])
            human.getModifier('measure/measure-calf-circ-decr|incr').setValue(self.df.iloc[i][21])
            human.getModifier('measure/measure-knee-circ-decr|incr').setValue(self.df.iloc[i][22])
            human.getModifier('measure/measure-ankle-circ-decr|incr').setValue(self.df.iloc[i][23])
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
