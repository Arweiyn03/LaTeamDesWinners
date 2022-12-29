import maya.cmds as cmds


def createWindow():
    
    #declaration de mes variables
    global slidernmbrchemins
    global slidertaillechemins
    global slidernombrebioms1
    global slidernombrebioms2
    global slidernombrebioms3
    global slidernombrebioms4
    
    #creation de ma fenetre    
    win = cmds.window("World Edit")
    cmds.rowColumnLayout(height=160,width=400,nc=2,cw=[(1,200),(2,200)])
    
    #creation de mes boutons    
    cmds.text(label="Nombre de chemins")
    slidernmbrchemins = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
    
    cmds.text(label="Tailles moyennes des chemins")
    slidertaillechemins = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
    
    cmds.text(label="Nombre d'arbre")
    slidernombrearbre = cmds.floatSliderGrp(min = 0.1, max = 0.5,sliderStep = 0.001,field = True, value = 0.2)
    
    cmds.text(label="Nombre de biomes type 1")
    slidernombrebioms1 = cmds.intSliderGrp(min = 0, max = 5,sliderStep = 1,field = True, value = 3)
    
    cmds.text(label="Nombre de biomes type 1")
    slidernombrebioms2 = cmds.floatSliderGrp(min = 0.2, max = 4,sliderStep = 1,field = True, value = 2)
    
    cmds.text(label="Nombre de biomes type 1")
    slidernombrebioms3 = cmds.intSliderGrp(min = 0, max = 12,sliderStep = 1,field = True, value = 1)
    
    cmds.button(label = "Edit World", c = "commandeNombreCailloux()")
    cmds.button(label = "Reset World", c = "ResetWorld()")
    
    return win
    
    
    
#verifier que la fenetre exist, sinon la creer (pour eviter les problemes de   
try : print (win)
except : win = ""

winExists = cmds.window(win, query=True, exists=True)

if winExists :
       cmds.showWindow(win);
        
else :
        cmds.showWindow(createWindow());
        
#ca sert a r pour le moment, c'est juste pour me souvenir des commandes qui fond echo au random        
from random import *
import random
        
