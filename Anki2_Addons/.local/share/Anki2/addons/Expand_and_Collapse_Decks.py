import sys
from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from PyQt4.QtGui import QAction, QProgressDialog 


def toggleDecksCollapsed(collapsed):
    "Toggles all decks to be either expanded or collapsed, based upon the boolean parameter passed in "
    # get all the decks and set them collapsed/expanded
    deckids = mw.col.decks.allIds()
    for deckid in deckids:
        deck = mw.col.decks.get(deckid)
        deck['collapsed'] = collapsed
        mw.col.decks.save(deck)
        
    # Refresh the browser to show the changes
    mw.deckBrowser.refresh()
        
        
def expandAllDecks():
    toggleDecksCollapsed(False)
    
    
def collapseAllDecks():
    toggleDecksCollapsed(True)
   
   
expandAction = QAction("Expand All Decks", mw)
mw.connect(expandAction, SIGNAL("triggered()"), expandAllDecks)
mw.form.menuTools.addAction(expandAction)

collapseAction = QAction("Collapse All Decks", mw)
mw.connect(collapseAction, SIGNAL("triggered()"), collapseAllDecks)
mw.form.menuTools.addAction(collapseAction)

