import maya.cmds as cmds

#creation de ma class onglet et de ma fonction fenetre
class tabs :    
    def __init__(createWindow):
        
        #declaration de mes variables
        global sliderEspaceMesh
        
        creationFenetre = cmds.window("La campagne c'est jolie")
        
        fileMenu = cmds.menu( label='File')
        cmds.menuItem( label='Open' )

        createWindow.tabs = cmds.tabLayout(width = 450,height = 185)
        fTab = cmds.rowColumnLayout('Edit World')
        
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [fTab,'Edit World'], tabPosition = "east")
        
        cmds.frameLayout( label='Interface',collapsable=False, collapse=False)
        cmds.setParent("..")
        
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 300)])
        
        cmds.text(label="Espace entre les mesh")
        sliderEspaceMesh = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20 )
        
        
        cmds.text(label="Espace entre les mesh")
        sliderespacemesh = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text(label="Resolution")
        sliderresolution = cmds.intSliderGrp(min = 0, max = 100,sliderStep = 1,field = True, value = 20)
        
        cmds.text( label='Mesh Principales')
        slidermeshprinc = cmds.floatSliderGrp(min = 0.1, max = 0.5,sliderStep = 0.001,field = True, value = 0.2)
        
        cmds.text(label="Nombre de biomes type 1")
        slidermap = cmds.intSliderGrp(min = 0, max = 5,sliderStep = 1,field = True, value = 3)
        
        cmds.setParent("..")
        
        """cmds.frameLayout( label='Mesh Disponible',collapsable=True, collapse=True)
        cmds.rowColumnLayout(numberOfColumns=2, columnWidth=[(1, 150), (2, 300)])"""
        
        cmds.frameLayout( label='Mesh Disponible',collapsable=True, collapse=True)
        
        cmds.rowColumnLayout(numberOfColumns=5, columnWidth=[(1, 75), (2, 75),(3, 75),(3, 75)],columnSpacing = [(1, 10), (2, 10),(3, 10), (4, 10)], rowSpacing = [(1, 10), (2, 10),(3, 10), (4, 10)])


        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.1.png")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.1.png")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.1.png" )
        cmds.text(label="chat")
        cmds.text(label="chat")
        cmds.text(label="chat")
        cmds.text(label="chat")   
        cmds.text(label="chat")      
        cmds.setParent("..")
        cmds.setParent("..")

        
        cmds.separator(height=20)
        cmds.rowColumnLayout('Edit ',numberOfColumns=2, columnWidth=[(1, 225), (2, 225)] , rowSpacing = [(1, 20), (2, 20)])
       
        
        cmds.button(label = "Edit World", c = "commandeNombreCailloux()")
        cmds.button(label = "Reset World", c = "ResetWorld()")
        
        cmds.setParent("..")
        cmds.setParent("..")
        
        
        sTab = cmds.rowColumnLayout(numberOfColumns=6, columnWidth=[(1, 150), (2, 150), (3, 150), ],columnSpacing = [(1, 10), (2, 10), (3, 10), (4, 10), (5, 10),(6,10)], rowSpacing = [(1, 10), (2, 10), (3, 10)],bgc=[0,0.7,0.2])
        cmds.tabLayout(createWindow.tabs, edit = True, tabLabel = [sTab,"Exemple d'images"])
        
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat2.png" )
        cmds.text(label="Ceci est un chat", hlc=[0,0.7,0.2])
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat4.png" )
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat2.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat3.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat4.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat1.png" )
        cmds.nodeIconButton( style='iconOnly', command='cmds.sphere()', image1="D:\LaTeamDesWinners\Interface\Images\chat2.png" )
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.text(label="Ceci est un chat")
        cmds.setParent("..")
        
        
        
        
        
        
        
        
        cmds.showWindow(creationFenetre)
        
tabs ()
        