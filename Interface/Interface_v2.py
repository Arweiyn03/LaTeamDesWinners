import maya.cmds as cmds

#creation de ma class onglet et de ma fonction fenetre
class tabs :    
    def __init__(createWindow):
        
        #declaration de mes variables
        global sliderespacemesh
        global sliderresolution
        global slidermeshprinc
        global slidermap

        #creation de ma fenetre    
        createWindow.win = cmds.window("La campagne c'est jolie")
        #cmds.rowColumnLayout(height=160,width=400,nc=2,cw=[(1,200),(2,200)])
        
 
        #Creation de mes onglet
        createWindow.tabs = cmds.tabLayout()
        

        #Creation de mon premier onglet et de son slider
        fTab = cmds.rowColumnLayout(numberOfColumns=3)
        
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [fTab,'Edit World'])    
        
        
        
  

        #Creation de mes boutons       
        cmds.text(label="Nombre de chemins")
        sliderespacemesh = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1, value = 20)
        
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        
        cmds.text(label="Tailles moyennes des chemins")
        sliderresolution = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Nombre d'arbre")
        slidermeshprinc = cmds.floatSliderGrp(min = 0.1, max = 0.5,sliderStep = 0.001,field = True, value = 0.2, bgc=[0,0.7,0.2])
        
        cmds.text(label="Nombre de biomes type 1")
        slidermap = cmds.intSliderGrp(min = 0, max = 5,sliderStep = 1,field = True, value = 3)
        
        cmds.button(label = "Edit World", c = "commandeNombreCailloux()")
        cmds.button(label = "Reset World", c = "ResetWorld()")
        
        cmds.setParent("..")
        
        
        #Creation de mon deuxieme onglet
        
        #sTab = cmds.scrollLayout(numberOfColumns=2)
        sTab = cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 150), (2, 150), (3, 150), ],columnSpacing = [(1, 10), (2, 10), (3, 10), (4, 10), (5, 10),(6,10)], rowSpacing = [(1, 10), (2, 10), (3, 10)],bgc=[0,0.7,0.2])
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [sTab,"Exemple d'images"])
        
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat2.png" )
        cmds.text(label="Ceci est un chat", hlc=[0,0.7,0.2])
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat4.png" )
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\chat2.png" )
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
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

        
