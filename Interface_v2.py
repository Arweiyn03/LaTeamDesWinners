import maya.cmds as cmds

#creation de ma class onglet et de ma fonction fenetre
class tabs :    
    def __init__(createWindow):
        
        #declaration de mes variables
        global slidernmbrchemins
        global slidertaillechemins
        global slidernombrebioms1
        global slidernombrebioms2
        global slidernombrebioms3
        global slidernombrebioms4
        
        #creation de ma fenetre    
        createWindow.win = cmds.window("La campagne c'est jolie")
        #cmds.rowColumnLayout(height=160,width=400,nc=2,cw=[(1,200),(2,200)])
        
        
        #Creation de mes onglet
        createWindow.tabs = cmds.tabLayout()

        #Creation de mon premier onglet et de son slider
        fTab = cmds.rowColumnLayout(numberOfColumns=2)
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [fTab,'Edit World']) 
        
        #Creation de mes boutons       
        cmds.text(label="Nombre de chemins")
        slidernmbrchemins = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Tailles moyennes des chemins")
        slidertaillechemins = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Nombre d'arbre")
        slidernombrearbre = cmds.floatSliderGrp(min = 0.1, max = 0.5,sliderStep = 0.001,field = True, value = 0.2)
        
        cmds.text(label="Nombre de biomes type 1")
        slidernombrebioms1 = cmds.intSliderGrp(min = 0, max = 5,sliderStep = 1,field = True, value = 3)
        
        cmds.text(label="Nombre de biomes type 2")
        slidernombrebioms2 = cmds.floatSliderGrp(min = 0.2, max = 4,sliderStep = 1,field = True, value = 2)
        
        cmds.text(label="Nombre de biomes type 3")
        slidernombrebioms3 = cmds.intSliderGrp(min = 0, max = 12,sliderStep = 1,field = True, value = 1)
        
        cmds.button(label = "Edit World", c = "commandeNombreCailloux()")
        cmds.button(label = "Reset World", c = "ResetWorld()")
        
        cmds.setParent("..")
        
        
        #Creation de mon deuxieme onglet
        #sTab = cmds.scrollLayout(numberOfColumns=2)
        sTab = cmds.rowColumnLayout(numberOfColumns=3)
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [sTab,"Exemple d'images"])
        
        cmds.paneLayout(configuration='quad', height = 300, width = 300, numberOfChildren=4)
        cmds.image(image="D:\LaTeamDesWinners\chat1.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat2.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat3.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat4.jpg")
        
        
        cmds.image(image="D:\LaTeamDesWinners\chat1.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat2.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat3.jpg")
        cmds.image(image="D:\LaTeamDesWinners\chat4.jpg")
        
        cmds.setParent("..")

        cmds.showWindow(createWindow.win)
        
tabs ()
  
#verifier que la fenetre exist, sinon la creer (pour eviter les problemes de   
"""try : print (win)
except : win = ""

winExists = cmds.window(win, query=True, exists=True)

if winExists :
       cmds.showWindow(win);
        
else :
        cmds.showWindow(createWindow());"""
        
#ca sert a r pour le moment, c'est juste pour me souvenir des commandes qui fond echo au random        
#from random import *
#import random

        
