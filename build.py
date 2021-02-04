from fontTools.ttLib.ttFont import newTable
from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil, subprocess, glob
from pathlib import Path

print ("[Train One] Generating TTFs")
__main__.main(("-g","sources/TrainOne.glyphs", "-o","ttf",))

for font in Path("master_ttf").glob("*.ttf"):
    modifiedFont = TTFont(font)
    print ("["+str(font).split("/")[1][:-4]+"] Adding stub DSIG")
    modifiedFont["DSIG"] = newTable("DSIG")     #need that stub dsig
    modifiedFont["DSIG"].ulVersion = 1
    modifiedFont["DSIG"].usFlag = 0
    modifiedFont["DSIG"].usNumSigs = 0
    modifiedFont["DSIG"].signatureRecords = []

    print ("["+str(font).split("/")[1][:-4]+"] Making other changes")
    modifiedFont["name"].addMultilingualName({'ja':'トレイン One'}, modifiedFont, nameID = 1, windows=True, mac=False)
    modifiedFont["name"].addMultilingualName({'ja':'Regular'}, modifiedFont, nameID = 2, windows=True, mac=False)
    modifiedFont["head"].flags |= 1 << 3        #sets flag to always round PPEM to integer
    modifiedFont["GDEF"].table.GlyphClassDef.classDefs = {"acutecomb": 3, "uni0306": 3, "uni0307": 3, "uni0308": 3, "uni030B": 3, "uni0328": 3, "uni030C": 3, "uni0305": 3, "acutecomb.rotat": 3, "uni0302.rotat": 3, "uni0306.rotat": 3, "uni0307.rotat": 3, "uni0308.rotat": 3, "uni030B.rotat": 3, "uni0328.rotat": 3, "uni030C.rotat": 3, "uni0305.rotat": 3}        #define mark glyph class in GDEF table
    
    modifiedFont.save("fonts/ttf/"+str(font).split("/")[1])

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")

for font in Path("fonts/ttf/").glob("*.ttf"):
    print ("["+str(font).split("/")[2][:-4]+"] Autohinting")
    fontName = str(font)
    hintedName = fontName[:-4]+"-hinted.ttf"
    subprocess.check_call(
        [
            "ttfautohint",
            "--stem-width",
            "nsn",
            fontName,
            hintedName,
        ]
    )

    shutil.move(hintedName, fontName)
