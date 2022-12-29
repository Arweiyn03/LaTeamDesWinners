import maya.cmds as cmds

#creation de ma class onglet et de ma fonction fenetre
class tabs :    
    def __init__(createWindow):
        
        #declaration de mes variables
        global sliderEspaceMesh
        
        #creation de ma fenetre et du premier onglet
        creationFenetre = cmds.window("La campagne c'est jolie")
        cmds.tabLayout()
        cmds.rowColumnLayout('Edit World',numberOfColumns=2, columnWidth=[(1, 300), (2, 150), (3, 150)])
        
        #creation de mon menu deroulent
        cmds.frameLayout( label='Interface',collapsable=False, collapse=False)
        
        #creation des slider
        cmds.text(label="Espace entre les mesh")
        sliderEspaceMesh = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20 )
        
        
        cmds.text(label="Espace entre les mesh")
        sliderespacemesh = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Resolution")
        sliderresolution = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Mesh Principale")
        slidermeshprinc = cmds.floatSliderGrp(min = 0.1, max = 0.5,sliderStep = 0.001,field = True, value = 0.2, bgc=[0,0.7,0.2])
        
        cmds.setParent( '..' )
        #creation de mon menu deroulent
        cmds.frameLayout( label='Mesh Disponibles',collapsable=False, collapse=False)
        
        cmds.text(label="Nombre de biomes type 1")
        slidermap = cmds.intSliderGrp(min = 0, max = 5,sliderStep = 1,field = True, value = 3)
        
        cmds.button(label = "Edit World", c = "commandeNombreCailloux()")
        cmds.button(label = "Reset World", c = "ResetWorld()")
        
        cmds.setParent("..")
        
        
        
        
        
        
        
        
        
        
        
        cmds.showWindow(creationFenetre)
        
tabs ()
        