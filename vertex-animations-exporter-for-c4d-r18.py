import c4d
import os
import subprocess
from c4d import gui

#OBJ SEQUENCE EXPORTER FOR PC2UNITY
#TESTED IN C4D R18

#USAGE:
#1) SET TIMELINE START-END
#2) SELECT OBJECTS TO EXPORT
#3) EXECUTE SCRIPT
#4) SELECT FILENAME. FRAME NUMBER WILL BE AUTOMATICALLY ADDED TO .OBJ FILE NAMES  


def main():
    c4d.StopAllThreads()
    doc = c4d.documents.GetActiveDocument()
    fps = doc.GetFps()
    fromTime = doc.GetMinTime().GetFrame(fps)
    toTime = doc.GetMaxTime().GetFrame(fps)
    animLength = toTime - fromTime + 1
    filePath = c4d.storage.SaveDialog()
    filePath, objName = os.path.split(filePath)
    objName = objName + "_"
    filePath = filePath + "\\"

    for f in range(0,animLength):
        doc.SetTime(c4d.BaseTime(fromTime,fps) + c4d.BaseTime(f,fps))
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW)
        c4d.DrawViews(c4d.DRAWFLAGS_FORCEFULLREDRAW)
            
        c4d.StatusSetText("Exporting " + str(f) + " of " + str(animLength))
        c4d.StatusSetBar(100.0*f/animLength)
             
        c4d.CallCommand(16768, 16768)  
        c4d.CallCommand(100004794, 100004794)  
        c4d.CallCommand(100004787) 
            
        fileName = filePath+objName+str(f)+".obj"
        savingresult = c4d.documents.SaveDocument(doc,fileName,c4d.SAVEDOCUMENTFLAGS_0,c4d.FORMAT_OBJ2EXPORT)
        
        c4d.CallCommand(12105, 12105)  
        c4d.CallCommand(12105, 12105)  
        c4d.CallCommand(12105, 12105)  
         
    c4d.StatusClear()
    gui.MessageDialog( 'Exporting to'+filePath+' done' )
 
    
if __name__=='__main__':
    main()