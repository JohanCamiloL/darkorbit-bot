import pyautogui
from random import randint
import time


def getImagePositionWithHighAccuracy(image):
    return pyautogui.locateCenterOnScreen(image, confidence=0.88)


def getImagePosition(image):
    return pyautogui.locateCenterOnScreen(image, confidence=0.8, grayscale=True)


def getImagePositionOnRegion(image, regionSearch):
    return pyautogui.locateCenterOnScreen(image, confidence=0.8, grayscale=True, region=regionSearch)


def getImagePositionAndSize(image):
    return pyautogui.locateOnScreen(image, confidence=0.8, grayscale=True)


def getImageAndClick(image, posX=0, posY=0):
    imgPosition = getImagePosition(image)
    pyautogui.moveTo(imgPosition.x + posX, imgPosition.y + posY, 1)
    pyautogui.click(imgPosition.x + posX, imgPosition.y + posY)
    time.sleep(0.5)


fullMap = getImagePositionAndSize('Full_Map.PNG')


def moveRandonOnMap():
    randomX = randint(fullMap.left + 3, fullMap.left + fullMap.width - 3)
    #randomY = randint(fullMap.top + 3, fullMap.top + fullMap.height - 3)
    randomY = randint(fullMap.top + 3, fullMap.top + 140)
    pyautogui.moveTo(randomX, randomY, 1)
    pyautogui.click(randomX, randomY)
    time.sleep(10)


def attackNpc(npcPos):
    pyautogui.click(npcPos.x + 60, npcPos.y - 60)
    time.sleep(0.5)
    pyautogui.press('ctrl')


def fullScreenGame():
    fullScreenButton = getImagePosition('Full_Screen_Button.PNG')
    allowButton = getImagePosition('Allow_Button.PNG')
    pyautogui.click(fullScreenButton.x, fullScreenButton.y)
    time.sleep(1)
    pyautogui.click(allowButton.x, allowButton.y)


def confPetToCollectBoxes():
    if (getImagePositionWithHighAccuracy('Repair_PET.PNG') != None):
        getImageAndClick('Repair_PET.PNG', 0, 30)
    elif (getImagePositionWithHighAccuracy('Button_Stop_PET.PNG') == None):
        getImageAndClick('Button_Play_PET.PNG')
        getImageAndClick('Pet_Menu.PNG')
        if (getImagePosition('Auto_recolector.PNG') == None):
            if (getImagePosition('Revivir_Lugar.PNG') != None):
                reviveOnPlace()
            elif (getImagePosition('Nueva_Conexion.PNG') != None):
                newConnection()
        else:
            getImageAndClick('Auto_recolector.PNG')


def repairPet():
    getImageAndClick('Repair_PET.PNG', 0, 30)
    pyautogui.moveTo(100, 100, 1)


def revivirOnPortal():
    getImageAndClick('Revivir_Portal.PNG')
    getImageAndClick('Boton_Revivir.PNG')


def reviveOnPlace():
    getImageAndClick('Revivir_Lugar.PNG')
    getImageAndClick('Boton_Revivir.PNG')
    time.sleep(2)


def newConnection():
    getImageAndClick('Nueva_Conexion.PNG')
    time.sleep(5)


while(True):
    if (getImagePositionWithHighAccuracy('Nueva_Conexion.PNG') != None):
        newConnection()
        confPetToCollectBoxes()
    elif (getImagePosition('Revivir_Lugar.PNG') != None):
        reviveOnPlace()
    elif (getImagePositionWithHighAccuracy('Repair_PET.PNG') != None):
        repairPet()
        confPetToCollectBoxes()
    elif (getImagePositionWithHighAccuracy('Button_Play_PET.PNG')):
        confPetToCollectBoxes()

    moveRandonOnMap()
