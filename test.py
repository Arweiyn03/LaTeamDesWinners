import maya.cmds as cmds

#cmds.file("chat1.jpg", i = True)


window = cmds.window()
cmds.paneLayout()
cmds.image( image='chat1' )
cmds.showWindow( window )
