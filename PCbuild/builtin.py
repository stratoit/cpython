from primitives import *
from math import *

def chr(val : int) -> str {}
def ord(val : str) -> int {}
def hit() {}
def exec() {}
def print(*args) {}
def print_test() {}
def type(obj) {}
def assert(condition) {}
def type2() {}
def hasattr(obj, findItem) {}
def getattr(obj, getItem) {}
def setattr(obj, setItem, setValue) {}
def delattr(obj, deleteItem) {}
def len(obj) -> int {}
def vars(obj) -> dict {}
def isinstance(value, cdo) {}
def format(val, formatType : str) -> str {}
def uuid_gen() {}
def storeman_sync(uuid: str, job : str, value : Variable) {}
def storeman_changeJob(jobName : str) {}
def storeman_connect(slotFunc) {}
def storeman_getjoblist() -> list{}
def storeman_getCurrentJob() -> str{}
def storeman_deleteAllColumnData() {}
def storeman_saveAs(str, str){}
def needDataRead() {}
def getUpdateIOList() {}
def getUpdateAxisList() {}
def projectPath() {}
def serialize(obj) -> str{}
def deserialize(strSerialized : str) {}
def dbQuery(query : str) {}
def UpdateLastIndex() {}
#def Query() {}
def open(strFile:str, strFlag:str) {}
def fatal(message: str,channel: str ){}
def debug(message: str,channel: str ){}
def error(message: str,channel: str ){}
def warning(message: str,channel: str ){}
def info(message: str,channel: str ){}
def super(){}
def listenToNotify(){}
def sleep(sec : double){}
def msleep(msec : double){}
def convert(type, obj) {}
def isBuild64bit() {}
def isBuildDebug() {}
def osEnviron(var: str) {}
def userman_login(id: str, pw: str) {}
def userman_connect(obj) {}
def userman_whoami() -> SUserInfo {}
def next(iterObj) -> nextObj {}

class Exception(){}

class Apple()
{
}

class QApplication()
{
}

class QMainWindow()
{
}

class SMutex()
{
	def lock(self) {}
	def unlock(self) {}
}

class set()
{
	def get(self){}
	def contains(self){}
	def add(self, addVal){}
	def clear(self){}
	def count(self) -> int {}
	def remove(self){}
}

class time()
{
	def sleep(self, sec: int){}
	def msleep(self, ms: int){}
}

class SPoint()
{
	def __init__(self, x:int, y:int){}

	def setX(self, x : int){}
	def setY(self, y : int){}

	def getX(self) -> int {}
	def getY(self) -> int {}

}

class SRowCol()
{
    def __init__(self, row : int, col : int)
    {
        self.data = SPoint(col, row)
    }
    
    def setRow(self, row : int)
    {
        self.data.setY(row)
    }
    def setColumn(self, column : int)
    {
        self.data.setX(column)
    }
    def getRow(self)
    {
        return self.data.getY()
    }
    def getColumn(self)
    {
        return self.data.getX()
    }
}

class SPointF()
{
	def __init__(self, x:float, y:float){}
	def setX(self, x : float){}
	def setY(self, y : float){}

	def getX(self) -> float {}
	def getY(self) -> float {}

	def add(self) -> float {}
}

class SRect()
{
	def setLeft(self, x:int){}
	def setTop(self, y:int){}
	def setRight(self, x:int){}
	def setBottom(self, y:int){}

	def getLeft(self){}
	def getTop(self){}
	def getRight(self){}
	def getBottom(self){}
	def contains(self){}

	def intersects(self){}
}

class SRectF()
{
	def __init__(self, x: float, y: float, width : float, height : float){}
	def setLeft(self, x: float){}
	def setTop(self, y: float){}
	def setRight(self, x: float){}
	def setBottom(self, y: float){}

	def getLeft(self){}
	def getTop(self){}
	def getRight(self){}
	def getBottom(self){}
	def contains(self){}

	def intersects(self){}
}

class SModelIndex()
{
	def setRow(self){}
	def setColumn(self){}

}

class SSize()
{
	def getWidth(self) {}
	def setWidth(self, val) {}
	def getHeight(self) {} 
	def setHeight(self, val) {}
}

class SWidget()
{
	def __init__(self, parent : SWidget)
	{
		self.moved = Signal()
		self.doubleClicked = Signal()
		self.leftClicked = Signal()
		self.rightClicked = Signal()
		self.leftReleased = Signal()
		self.enter = Signal()
		self.leave = Signal()
		self.hoverEnter = Signal()
		self.hoverLeave = Signal()
		self.keyPress = Signal()
		self.keyRelease = Signal()
		self.focusIn = Signal()
		self.focusOut = Signal()
		self.resize = Signal()
		self.inputMethodQuery = Signal()
		self.customContextMenuRequested = Signal()
		self.windowIconChanged = Signal()
		self.windowTitleChanged = Signal()
		self.hideEvent = Signal()
		self.closeEvent = Signal()
		self.scroll = Signal()
		self.showEvent = Signal()
	}
	def setObjectName(self, objName : str) {}
	def raise2(self)
	{}
	def show(self)
	{}
	def hide(self)
	{}
  	def setX(self, x : int)
	{}
	def setY(self, y : int)
	{}
	def setWidth(self, width : int)
	{}
	def setHeight(self, height : int)
	{}
	def setEnable(self, enable : bool)
	{}
	def setFontFamily(self, fontFamily : str)
	{}
	def setFontSize(self, size : int)
	{}
	def setFontWeight(self, weight : int)
	{}
	def setFontItalic(self, italic : bool)
	{}
	def setCursorShape(self, shape : int)
	{}
  	def setWindowTitle(self, title : str)
  	{}

	def setMinimumWidth(self, minimumWidth : int)
	{}
	def setMinimumHeight(self, minimumHeight : int)
	{}
	def setMaximumWidth(self, maximumWidth : int)
	{}
	def setMaximumHeight(self, maximumHeight : int)
	{}

	def update(self)
	{}
	def getWidth(self)
	{}
	def getHeight(self)
	{}
	def setFixedWidth(self, fixedWidth : int)
	{}
	def setFixedHeight(self, fixedHeight : int)
	{}
	def setStyleSheet(self, style : str)
	{}
	def setFill(self, fill : bool)
	{}

	def setTitle(self, title : str)
	{}
	def setUnit(self, unit : Unit)
	{}

	def onTimer(self)
	{}
	def close(self)
	{}
    def isVisible(self)
    {}
    def isEnable(self) -> bool
    {}

	def windowTitle(self) -> str
	{}
	def setDisabled(self, disable : bool)
	{}
	def setHidden(self, hidden : bool)
	{}
	def setVisible(self, visible : bool)
	{}
	def toolTip(self) -> str
	{}
	def toolTipDuration(self) -> int
 	{}

	def setAutoFillBackground(self, enabled: bool)
	{}

	def addAction(self, action: str)
	{}

	def setMarginLeft(self, margin : int)
	{}

	def setMarginTop(self, margin : int)
	{}

	def setMarginRight(self, margin : int)
	{}

	def setMarginBottom(self, margin : int)
	{}

	def setParent(self, parent : SWidget)
	{}

	def setHeightIncrement(self, height : int)
	{}

	def setWidthIncrement(self, width : int)
	{}

	def setFocus(self)
	{}

	def activateWindow(self)
	{}

	def adjustSize(self)
	{}

	def clearFocus(self)
	{}

	def showFullScreen(self)
	{}

	def showMaximized(self)
	{}

	def showMinimized(self)
	{}

	def showNormal(self)
	{}

	def hasFocus(self) -> bool
	{}

	def isActiveWindow(self) -> bool
	{}

	def isFullScreen(self) -> bool
	{}

	def isHidden(self) -> bool
	{}

	def isWindow(self) -> bool
	{}

	def isMaximized(self) -> bool
	{}

	def isMinimized(self) -> bool
	{}

	def isModal(self) -> bool
	{}

	def setToolTipDuration(self, msec : int)
	{}

	def autoFillBackground(self)
	{}

	def moveSync(self, dx : int, dy : int)
	{}

	def focusWidget(self) -> SWidget
	{}

	def childAt(self, point : SPoint) -> SWidget
	{}

	def parentWidget(self) -> SWidget
	{}

	def maximumSize(self) -> SSize
	{}

	def minimumSize (self) -> SSize
	{}

	def pos(self) -> SPoint
	{}

	def mapFrom(self, parent : SWidget, pos : SPoint) -> SPoint
	{}

	def mapTo(self, parent : SWidget, pos : SPoint) -> SPoint
	{}

	def mapFromGlobal(self, pos : SPoint) -> SPoint
	{}

	def mapFromParent(self, pos : SPoint) -> SPoint
	{}

	def mapToGlobal(self, pos : SPoint) -> SPoint
	{}

	def mapToParent(self, pos : SPoint) -> SPoint
	{}

	def setHorizontalSizePolicy(self, policy : str)
	{}

	def setVerticalSizePolicy(self, policy : str)
	{}
	
	def winId(self)
	{}
}

class Pixmap()
{
	def scaled(self, w, h, am, m)
	{}
}

class SBindable(SWidget)
{
	def createEmptyWidget(self)
	{

	}
}
class SAbstractButton(SWidget)
{
  	def __init__(self, parent : SWidget)
  	{
		self.parent = parent
		self.clicked = Signal()
		self.pressed = Signal()
  	}
	def click(self)
	{}
	def toggle(self)
	{}
	def setText(self, text : str)
	{}
	def setIconFile(self, filePath : str)
	{}
	def setIconWidth(self, width : int)
	{}
	def setIconHeight(self, height : int)
	{}
	def setCheckable(self, checkable : bool)
	{}
	def setCheck(self, check : bool)
	{}
	def getCheck(self) -> bool
	{}
	def getText(self) -> str
	{}
	def isCheckable(self) -> bool
	{}
	def isDown(self) -> bool
	{}
	def setDown(self, down : bool)
	{}
	def setChecked(self, checked : bool)
	{}
}

class SPushButton(SAbstractButton)
{
	def __init__(self, parent : SWidget)
	{
		SAbstractButton.__init__(self, parent)
		
		self.activate = Signal()
	}
	
	def setDelayed(delayed: bool) {}
	def isDelayed() -> bool {}
	
	def setDelayedTime(ms: int) {}
	def getDelayedTime() -> int {}
}

class SCheckBox(SWidget)
{
	def __init__(self, SWidget)
	{
		self.clicked = Signal()
	}
	def show(self){}
	def setCheck(self, check : bool){}
	def setCheckable(self, checkable : bool){}
	def setText(self, text : str){}
	def isTristate(self) -> bool {}
	def setTristate(self, y : bool){}
}

class SComboBox(SWidget)
{
	def __init__(self, parent : SWidget)
	{
		self.currentTextChanged = Signal()
    	self.activated = Signal()
        self.textActivated = Signal()
        self.currentIndexChanged = Signal()
        self.editTextChanged = Signal()
       	self.highlighted = Signal()
       	self.textHighlighted = Signal()
	}
	def setEditable(self, editable : bool)
	{}
	def setCurrentIndex(self, curIndex : int)
	{}
	def setIconWidth(self, iconWidth : int)
	{}
	def addItem(self, item : str)
	{}
	def itemText(self, itemIdx : int)
	{}
	def setMaxVisibleItems(self, val : int)
	{}
	def clear(self)
	{}
	def removeItem(self, index : int)
	{}
	def setLineEdit(self, lineEdit : SLineEdit)
	{}
	def count(self) -> int
	{}
	def currentIndex(self) -> int
	{}
	def duplicatesEnabled(self) -> bool
	{}
	def hasFrame(self) -> bool
	{}
	def hidePopup(self)
	{}
	def insertSeparator(self, index : int)
	{}
	def isEditable(self) -> bool
	{}
	def maxCount(self) -> int
	{}
	def maxVisibleItems(self) -> int
	{}
	def minimumContentsLength(self) -> int
	{}
	def setDuplicatesEnabled(self, enable : bool)
	{}
	def setFrame(self, b : bool)
	{}
	def setMaxCount(self, max : int)
	{}
	def setMinimumContentsLength(self, characters: int)
	{}
	def showPopup(self)
	{}
	def clearEditText(self)
	{}
	def currentText(self) -> str
	{}
	def insertItem(self,index :int, text : str) -> str
	{}
	def setItemText(self,index :int, text : str) -> str
	{}
	def setEditText(self, text : str) -> str
	{}
}

class SFormLayout()
{
	def setVerticalSpacing(self, spacing : int){}
	def setHorizontalSpacing(self, spacing : int){}
	def setVerticalStretch(self, stretch : list){}
	def setIndexMapping(self, indexList : list){}
	def setRow(self){}
	def setLabelWidth(self){}
	def addRow(self, labelText : str, field : SWidget){}
	def addRow(self, label : SWidget, field : SWidget){}
	def addRow(self, widget : SWidget){}
	def rowCount(self) -> int {}
	def setSpacing(self, spacing : int){}
	def spacing(self) -> int {}
	def verticalSpacing(self) -> int {}
	def horizontalSpacing(self) -> int {}
	def insertRow(self, row : int, label : SWidget, field : SWidget) {}
	def insertRow(self, row : int, label : str, field : SWidget){}
	def insertRow(self, row : int, widget : SWidget){}
	def insertRow(self, field : SWidget){}
	def labelForField(self, field : SWidget) -> SWidget {}
}

class SFrame(SWidget)
{
	def setLineWidth(self, lineWidth : int)
	{}
	def setMidLineWidth(self, midLineWidth : int)
	{}
	def setFrameShape(self, frameShape : int)
	{}
	##def setFrameWidth(self, frameWidth : int)
	##{}
	def setFrameStyle(self, frameStyle : int)
	{}
	def frameStyle(self) -> int
	{}
	def frameWidth(self) -> int
	{}
	def LineWidth(self) -> int
	{}
	def midLineWidth(self) -> int
	{}
}

class SStackedWidget(SFrame)
{
	def addWidget(self, SWidget) {}
    def count(self) {}
    def setCurrentIndex(self, index : int) {}
	def getCurrentIndex(self) -> int {}
}

class SLayout(SWidget)
{
	def setMarginLeft(self, margin : int)
	{}
	def setMarginTop(self, margin : int)
	{}
	def setMarginRight(self, margin : int)
	{}
	def setMarginBottom(self, margin : int)
	{}
	def addChild(self, child : SWidget)
	{}
	def removeChild(self, child : SWidget)
	{}
	def activate(self) -> bool
	{}
	def count(self) -> int
	{}
	def menuBar(self) -> SWidget
	{}
	def parentWidget(self) -> SWidget
	{}
	def setEnabled(self, enable : bool)
	{}
	def setSpacing(self, spacing : bool)
	{}
	def spacing(self) -> int
	{}
	def update(self)
	{}
	def invalidate(self)
	{}
	def isEmpty(self) -> bool
	{}
	def maximumSize(self) -> SSize
	{}
	def minimumSize(self) -> SSize
	{}
	def indexOf(self, widget : SWidget) -> int
	{}
	def setMenuBar(self, widget : SWidget)
	{}
}

class SGridLayout(SLayout)
{
	def setVerticalSpacing(self, spacing : int)
	{}
	def setHorizontalSpacing(self, spacing : int)
	{}
	def setVerticalStretch(self, verticalStretch : list)
	{}
	def setHorizontalStretch(self, horizontalStretch : list)
	{}
	def setIndexMapping(self, indexList : list)
	{}
	def setRow(self, row : int)
	{}
	def setColumn(self, col : int)
	{}
	def addChild(self, widget : SWidget, row : int, col : int)
	{}
	def addLayout(self, idx : int, layout : SLayout)
	{}
	def columnCount(self) -> int
	{}
	def columnMinimumWidth(self, column : int) -> int
	{}
	def columnStretch(self, column : int) -> int
	{}
	def horizontalSpacing(self) -> int
	{}
	def rowCount(self) -> int
	{}
	def rowMinimumHeight(self, row : int) -> int
	{}
	def rowStretch(self, row : int) -> int
	{}
	def setColumnMinimumWidth(self, column : int, minSize : int)
	{}
	def setRowMinimumHeight(self, row : int, minSize : int)
	{}
	def verticalSpacing(self) -> int
	{}
	def setSpacing(self, spacing : int)
	{}
	def spacing(self) -> int
	{}

}

class SGroupBox(SWidget)
{
	def setTitle(self, title : str)
	{}
	def setHorizontalAlignment(self, align : int)
	{}
	def setVerticalAlignment(self, align : int)
	{}
	def setCheckable(self, checkable : bool)
	{}
	def isCheckable(self) -> bool
	{}
	def isChecked(self) -> bool
	{}
	def isFlat(self) -> bool
	{}
	def setFlat(self, flat : bool)
	{}
	def title(self) -> str
	{}
	def setChecked(self, checked : bool)
	{}

}

class SBoxLayout(SLayout)
{
	def setLayoutSpacing(self, spacing : int)
	{}
	def setLayoutStretch(self, stretch : list)
	{}
	def addSpacerItem(self, spacer : SSpacerItem)
	{}
	def addLayout(self, layout : SLayout)
	{}
	def addStretch(self, streach : int)
	{}
	def addStrut(self, size : int)
	{}
	def insertSpacing(self, index : int, size : int)
	{}
	def insertStretch(self, index : int, stretch : int)
	{}
	def stretch(self, index : int) -> int
	{}
	def setStretchFactor(self, widget : SWidget, stretch : int) -> bool
	{}
	def insertChild(self, index : int, widget : SWidget) {}
}

class SHorizontalLayout(SBoxLayout)
{
}

class SLabel(SFrame)
{
	def setHorizontalAlignment(self, horizontalAlignment : int)
	{}
	def setVerticalAlignment(self, verticalAlignment : int)
	{}
	def setMargin(self, margin : int)
	{}
	def setText(self, text : str)
	{}
	##def setMidLineHeight(self)
	##{}
	def text(self) -> str
	{}
	def setPixmap(self, filePath : str)
	{}
	def setBuddy(self, buddy : SWidget)
	{}
	def buddy(self) -> SWidget
	{}
	def hasScaledContents(self) -> bool
	{}
	def hasSelectedText(self) -> bool
	{}
	def indent(self) -> int
	{}
	def margin(self) -> int
	{}
	def openExternalLinks(self) -> bool
	{}
	def selectedText(self) -> str
	{}
	def selectionStart(self) -> int
	{}
	def setIndent(self, indent : int)
	{}
	def setOpenExternalLinks(self, open : bool)
	{}
	def setScaledContents(self, scaled : bool)
	{}
	def setSelection(self, start : int, length : int)
	{}
	def setWordWrap(self, on : bool)
	{}
	def wordWrap(self) -> bool
	{}
	def clear(self)
	{}
	def setNum(self, num : int)
	{}
}

class SLineEdit(SWidget)
{
	def __init__(self, parent : SWidget)
	{
		self.keyPress = Signal()
		self.cursorPositionChanged = Signal()
		self.editingFinished = Signal()
		self.inputRejected = Signal()
		self.returnPressed = Signal()
		self.selectionChanged = Signal()
		self.textChanged = Signal()
		self.textEdited = Signal()
	}
	def backspace(self)
	{}
	def del(self)
	{}
	def cursorPosition(self) -> int
	{}
	def deselect(self)
	{}
	def displayText(self) -> str
	{}
	def dragEnabled(self) -> bool
	{}
	def end(self, mark : bool)
	{}
	def hasAcceptableInput(self) -> bool
	{}
	def hasFrame(self) -> bool
	{}
	def hasSelectedText(self) -> bool
	{}
	def home(self, mark : bool)
	{}
	def inputMask(self) -> str
	{}
	def insert(self)
	{}
	def isClearButtonEnabled(self) -> bool
	{}
	def isModified(self) -> bool
	{}
	def isReadOnly(self) -> bool
	{}
	def isRedoAvailable(self) -> bool
	{}
	def isUndoAvailable(self) -> bool
	{}
	def placeholderText(self) -> str
	{}
	def selectedText(self) -> str
	{}
	def selectionEnd(self) -> int
	{}
	def selectionLength(self) -> int
	{}
	def selectionStart(self) -> int
	{}
	def setClearButtonEnabled(self, enable : bool)
	{}
	def setCursorPosition(self, pos : int)
	{}
	def setText(self, text : str)
	{}
	def setReadOnly(self, readOnly: bool)
	{}
	def setAlignment(self, alignment : int)
	{}
	def getText(self) -> str
	{}
	def setMaxLength(self, maxLength : int)
	{}
	def getMaxLength(self) -> int
	{}
	def setFrame(self, frame : bool)
	{}
	def setDragEnabled(self, b : bool)
	{}
	def setInputMask(self,inputMask: QString)
	{}
	def setModified(self, b : bool)
	{}
	def setPlaceholderText(self, placeholder: QString)
	{}
	def setSelection(self, start : int, length : int)
	{}

}

class SListWidgetItem()
{
    def clone(self) {}
    def setText(self, text : str) {}
    def setHidden(self, hide : bool) {}
    def setIcon(self, icon : SIcon) {}
    def setData(self, role : int, value : obj) {}
    def setSelected(self, select : bool) {}
    def setTextAlignment(self, alignment : int) {}
    def setToolTip(self, toolTip : str) {}
    def isHidden(self) {}
    def isSelected(self) {}
    def getData(self, role : int) {}
    def getText(self) {}
    def getTextAlignment(self) {}
    def getToolTip(self) {}
    def getType(self) {}
    def setIcon(self, icon : SIcon) {}
}

class SListWidget(SWidget)
{
	def __init__(self, parent : SWidget)
	{
	}
	def setFlow(self, flow : int){}
	def setSpacing(self, space : int){}
	def setViewMode(self, mode : int){}
	def setTextAlignment(self, alignment : int){}
	def addItem(self, item : str){}
}

class SRadioButton(SAbstractButton)
{
}

class SVerticalLayout(SBoxLayout)
{
}

class STabWidget(SWidget)
{
	def setCurrentIndex(self, index : int){}
	def addTab(self, widget : SWidget, title : str){}
	def setTabText(self, index : int, tabName : str){}
	def clear(self){}
	def setMovable(self, movable : bool){}
	def count(self) -> int {}
	def currentIndex(self) -> int {}
	def isMovable(self) -> bool {}
	def isTabEnabled(self, index : int) -> bool {}
	def removeTab(self, index : int){}
	def setTabBarAutoHide(self, enabled : bool){}
	def setTabEnabled(self, index : int, enable : bool){}
	def setTabsClosable(self, closeable : bool){}
	def setUsesScrollButtons(self, useButtons : bool){}
	def tabText(self, index : int) -> str {}
	def tabToolTip(self, index : int) -> str {}
	def tabsClosable(self) -> bool {}
	def usesScrollButton(self) -> bool {}
	def currentWidget(self) -> SWidget {}
	def widget(self, index : int) -> SWidget {}
	def setCurrentWidget(self, widget : SWidget) {}
	def indexOf(self, widget : SWidget) -> int {}
	def setCurrentWidget(self, index : int, widget : SWidget, label : str) -> int {}
}

class SBrush()
{
	def setColor(self, r : int, g: int, b :int , a: int){}
	def setStyle(self, style : int){}

}

class SColor()
{
	def setRgb(self, r :int, g : int, b : int, a : int){}
	def red() -> int {}
	def blue() -> int {}
	def green() -> int {}
	def alpha() -> int {}
}

class SPen()
{
	def setColor(self, r : int, g: int, b :int , a: int){}
	def setWidth(self, width : int){}
	def setStyle(self, style : int){}
	def setBrush(self, brush : SBrush) {}
}

class SPainter()
{
	def drawLine(self, pointA : SPoint, pointB : SPoint){}
	def drawLineF(self, pointA : SPointF, pointB : SPointF){}
	def drawRect(self, LeftTopPoint : SPoint, RightBottomPoint : SPoint){}
	def drawRectF(self, LeftTopPoint : SPointF, RightBottomPoint : SPointF){}
	def drawText(self, pointA : SPointF, pointB : SPointF, text : str){}
	def setPen(self, pen: SPen){}
	def setBrush(self, brush: SBrush){}
	def setOpacity(self, opacity : float) {}

}

class SAbstractItemView(SWidget)
{
	def setAutoScroll(self, autoScroll : bool)
	{}
	def setSelectionMode(self, mode : int)
	{}
	def setAlternatingRowColors(self, enable : bool)
	{}
	def alternatingRowColors(self) -> bool
	{}
	def autoScrollMargin(self) -> int
	{}
	def currentIndex(self) -> SModelIndex
	{}
	def dragDropOverwriteMode(self) -> bool
	{}
	def dragEnabled(self) -> bool
	{}
	def hasAutoScroll(self) -> bool
	{}
	def indexAt(self, point : SPoint) -> SModelIndex
	{}
	def keyboardSearch(self, search : str)
	{}
	def resetHorizontalScrollMode(self)
	{}
	def resetVerticalScrollMode(self)
	{}
	def rootIndex(self) -> SModelIndex
	{}
	def setAutoScrollMargin(self, margin : int)
	{}
	def setDragDropOverwriteMode(self, overwrite : bool)
	{}
	def setDragEnabled(self, enable : bool)
	{}
	def setDropIndicatorShown(self, enable : bool)
	{}
	def setTabKeyNavigation(self, enable : bool)
	{}
	def showDropIndicator(self) -> bool
	{}
	def sizeHintForColumn(self, column : int) -> int
	{}
	def sizeHintForRow(self, row : int) -> int
	{}
	def tabKeyNavigation(self) -> bool
	{}
}

class STableWidget(SAbstractItemView)
{
	def __init__(self, parent : SWidget)
  	{
    		self.cellClicked = Signal()
  	}
	def setRow(self, row : int)
	{}
	def setColumn(self, column : int)
	{}
	def setHeader(self, index : int, headerName : str)
	{}

	def setItem(self, row : int, column : int, name : str){}
	def item(self, row: int, col: int) {}

	def removeRows(self){}

	def rowCount(self) -> int {}

	def columnCount(self) -> int {}

	def ResizeColumnToContent(self, column : int) {}

	def setCellWidget(self, row : int, column : int, item : SWidget){}

	def setCurrentCell(self, row : int, column : int) {}

	def cellWidget(self, row : int, column : int) {}

	def currentColumn(self) -> int {}

	def currentItem(self) -> STableWidget {}

	def currentRow(self) -> int {}

	def horizontalHeaderItem(self, column : int) -> STableWidget {}

	def itemAt(self, ax : int, ay : int) -> STableWidget {}

	def itemPrototype(self) -> STableWidget {}

	def removeCellWidget(self, row : int, column : int) {}

	def setColumnCount(self, columns : int) {}

	def takeHorizontalHeaderItem(self, column : int) -> STableWidget {}

	def takeItem(self, row : int, column : int) -> STableWidget {}

	def takeVerticalHeaderItem(self, row : int) -> STableWidget {}

	def verticalHeaderItem(self, row : int) -> STableWidget {}

	def visualColumn(self, logicalColumn : int) -> int {}

	def visualRow(self, logicalRow : int) -> int {}

	def clear(self) {}

	def clearContents(self) {}

	def insertColumn(self, column : int) {}

	def insertRow(self, row : int) {}

	def removeColumn(self, column : int) {}

	def removeRow(self, row : int) {}
}

class SIcon()
{	
	def __init__(self, filePath : self) {}
	def addFile(self, fileName : str) {}
	def addPixmap(self, fileName : str) {}
}

class SFileIconProvider() {	
	Computer = 0
	Desktop = 1
	Trashcan = 2
	Network = 3
	Drive = 4
	Folder = 5
}
class STreeWidgetItem()
{
	def addChild(self, child : STreeWidgetItem){}
	def setText(self, column : int, text : str){}
	def setExpanded(self, expand : bool){}
	def removeChild(self, child : STreeWidgetItem){}
	def child(self, index : int) -> STreeWidgetItem {}
	def childCount(self) -> int {}
	def clone(self) -> STreeWidgetItem {}
	def columnCount(self) -> int {}
	def isDisabled(self) -> bool {}
	def isExpanded(self) -> bool {}
	def isFirstColumnSpanned(self) -> bool {}
	def isHidden(self) -> bool {}
	def isSelected(self) -> bool {}
	def parent(self) -> STreeWidgetItem {}
	def setDisabled(self, disabled : bool) {}
	def setFirstColumnSpanned(self, span : bool) {}
	def setHidden(self, hide : bool){}
	def setSelected(self, select : bool){}
	def setIcon(self, column : int, icon : SIcon) {}
	def setTextAlignment(self, column : int, alignment : int) {}
	def setToolTip(self, column : int, tooltip : str) {}
	def text(self, column : int) -> str {}
	def textAlignment(self, column : int) -> int {}
	def toolTip(self, column : int) -> str {}
	def type(self) {}
	def setData(self, column : int, role : int, data : obj) {}
	def getData(self, column : int, role : int) -> obj {}
}

class STreeWidget(SAbstractItemView)
{
	def addTopLevelItem(self, item : STreeWidgetItem){}
	def setColumn(self, column : int){}
	def setHeader(self, column : int, header : str){}
	def collapseAll(self){}
	def expandAll(self){}
	def setCurrentItem(self, item : STreeWidgetItem){}
	def removeItemWidget(self, column: int, item : STreeWidgetItem){}
	def columnCount(self) -> int {}
	def sortColumn(self) -> int {}
	def topLevelItemCount(self) -> int {}
	def clear(self) {}
	def closePersistentEditor(self, item : STreeWidgetItem, column : int  ) {}
	def currentColumn(self) -> int {}
	def currentItem(self) -> STreeWidgetItem {}
	def editItem(self, item : STreeWidgetItem, column : int  ) {}
	def headerItem(self) -> STreeWidgetItem {}
	def indexOfTopLevelItem(self, item : STreeWidgetItem) -> int {}
	def insertTopLevelItem(self, column: int, item : STreeWidgetItem){}
	def invisibleRootItem(self) -> STreeWidgetItem {}
	def itemAbove(self, item : STreeWidgetItem) -> STreeWidgetItem {}
	def itemAt(self, point : SPoint) -> STreeWidgetItem {}
	def dragStart(self, item : STreeWidgetItem) {}
	def clearSelection(self) {}
	def useDrag(self, use : bool) {}
}

class SUserInfo()
{
	def setPermissionLevel(self, nPermissionLevel : int) {}
	def getPermissionLevel(self) -> int {}
	
	def setID(self, strID : str) {}
	def getID(self) -> str {}

	def setPW(self, strPW : str) {}
	def getPW(self) -> str {}
}

class Mutable()
{
	def __init__(self, instance)
	{
		self.instance = instance
		self.signalDataChanged = Signal()
		self.mutex = SMutex()
	}

	def read(self)
	{
	}

	def write(self)
	{
	}
}

class SDialog(SBindable)
{
	def reject(self){}
	def done(self, r : int){}

	def exec(self){}
	def setModal(self, modal: bool ){}
	def setResult(self, i : int){}
}

class SMessageBox(SWidget)
{
	def __init__(self, parent :SWidget)
	{
		self.buttonClicked = Signal()
	}
	def setWindowTitle(self, title : str) {}
	def setText(self, text : str) {}
	def exec(self) {}
	def show(self) {}
	def setStandardButtons(self, buttons: int) {}
}

class STimer()
{
	def start(self, time: int) {}
	def connect(self, function) {}
	def stop(self) {}
	def setSingleShot(self, var) {}
}

class sliced_cube()
{
	def __init__(self, c: cube, depth: int)
	{
		self.c: cube = c
		self.depth: int = depth
	}

	def get(self, row: int, col: int)
	{
		return self.c.get(row, col, self.depth)
	}

	def set(self, row: int, col: int, value)
	{
		self.c.set(row, col, self.depth, value)
	}
}

class MutableStr(Mutable)
{
	def __init__(self, text: str)
	{
		Mutable.__init__(self, text)
		self.instance : str = self.instance

		self.text : str = ""
	}

	def read(self)
	{
		self.mutex.lock()
		self.text = self.instance
		self.mutex.unlock()
	}

	def write(self, data : str)
	{
		self.mutex.lock()
		self.instance = data
		self.mutex.unlock()
		self.signalDataChanged.emit()
	}

}

class RichMessageBox(SMessageBox)
{
	class StandardButton()
	{
		Escape = 512
		Ok = 1024
		Save = 2048
		Yes = 16384
		No = 65536
		Cancel = 4194304‬
		Ok_Cancel = 4195328
        NoButton = 0
        Close = 2097152
        Default = 256
	}

	def __init__(self)
	{
		self.mutableData : MutableStr = None
        self.sigOKCancel = Signal()
		self.uuid = None
	}

	def setMutableStr(self, mutable : MutableStr)
	{
		self.mutableData = mutable
		self.updateText()
		self.mutableData.signalDataChanged.connect(self.updateText)
	}
	def setUUid(self, uuid : str)
	{
		self.uuid = uuid
	}

	def updateText(self)
	{
		self.mutableData.read()
		self.setText(self.mutableData.text)
	}

    def checkButton(self, button:int)
    {
        if(None == button)
        {
           self.sigOKCancel.emit(BasicMessages.MsgStop())
        }
        if(RichMessageBox.StandardButton.Ok == button)
        {
            self.sigOKCancel.emit(MessageBox.Ok())
        }            
        if(RichMessageBox.StandardButton.Cancel == button)
        {
            self.sigOKCancel.emit(MessageBox.Cancel())
        }
    }
    
    def slotClose(self)
    {
        self.sigOKCancel.emit(MessageBox.Cancel())
    }
}

class SNumpadReal(SDialog)
{

		def __init__(self, parent: SWidget, min: float, max: float, default: float)
		{
			self.min=min
			self.max=max
			self.default=default

            self.onCancel = Signal()
            self.onCancelWithSender = Signal()
            self.onOk = Signal()
            self.onOkWithSender = Signal()
            self.textNoFormat = str(self.default)

            self.firstInput = true

			self.setX(0)
			self.setY(0)
			self.setWidth(274)
			self.setHeight(333)
			self.setEnable(true)
			self.setFontFamily("Gulim")
			self.setFontSize(9)
			self.setFontWeight(50)
			self.setFontItalic(false)
			self.setCursorShape(0)
			self.setWindowTitle("Numpad Real")
			self.verticalLayout=SVerticalLayout(self)
			self.verticalLayout.setX(6)
			self.verticalLayout.setY(6)
			self.verticalLayout.setWidth(259)
			self.verticalLayout.setHeight(320)
			self.verticalLayout.setEnable(true)
			self.verticalLayout.setFontFamily("Gulim")
			self.verticalLayout.setFontSize(9)
			self.verticalLayout.setFontWeight(50)
			self.verticalLayout.setFontItalic(false)
			self.verticalLayout.setCursorShape(0)
			self.verticalLayout.setMarginLeft(10)
			self.verticalLayout.setMarginTop(10)
			self.verticalLayout.setMarginRight(10)
			self.verticalLayout.setMarginBottom(10)
			self.verticalLayout.setLayoutSpacing(0)
			self.verticalLayout.setLayoutStretch([1,5])
			self.lineEdit=SLineEdit(self.verticalLayout)
			self.lineEdit.setX(10)
			self.lineEdit.setY(10)
			self.lineEdit.setWidth(239)
			self.lineEdit.setHeight(50)
			self.lineEdit.setEnable(true)
			self.lineEdit.setFontFamily("Gulim")
			self.lineEdit.setFontSize(9)
			self.lineEdit.setFontWeight(50)
			self.lineEdit.setFontItalic(false)
			self.lineEdit.setCursorShape(0)
			self.lineEdit.setText("")
			self.lineEdit.setReadOnly(true)
			self.lineEdit.setAlignment(2)

			self.verticalLayout.addChild(self.lineEdit)
			self.gridLayout=SGridLayout(self.verticalLayout)
			self.gridLayout.setX(10)
			self.gridLayout.setY(60)
			self.gridLayout.setWidth(239)
			self.gridLayout.setHeight(250)
			self.gridLayout.setEnable(true)
			self.gridLayout.setFontFamily("Gulim")
			self.gridLayout.setFontSize(9)
			self.gridLayout.setFontWeight(50)
			self.gridLayout.setFontItalic(false)
			self.gridLayout.setCursorShape(0)
			self.gridLayout.setMarginLeft(0)
			self.gridLayout.setMarginTop(10)
			self.gridLayout.setMarginRight(0)
			self.gridLayout.setMarginBottom(10)
			self.gridLayout.setVerticalSpacing(10)
			self.gridLayout.setHorizontalSpacing(10)
			self.gridLayout.setVerticalStretch([0,0,0,0,0,0,0])
			self.gridLayout.setHorizontalStretch([0,0,0])
			self.gridLayout.setIndexMapping([21,18,19,20,15,12,9,6,16,13,17,14,11,10,7,8,0,3,1,4])
			self.gridLayout.setRow(4)
			self.gridLayout.setColumn(7)
			self.verticalLayout.addChild(self.gridLayout)
			self.pushButton_0=SPushButton(self.gridLayout)
			self.pushButton_0.setX(0)
			self.pushButton_0.setY(215)
			self.pushButton_0.setWidth(73)
			self.pushButton_0.setHeight(24)
			self.pushButton_0.setEnable(true)
			self.pushButton_0.setFontFamily("Gulim")
			self.pushButton_0.setFontSize(9)
			self.pushButton_0.setFontWeight(50)
			self.pushButton_0.setFontItalic(false)
			self.pushButton_0.setCursorShape(0)
			self.pushButton_0.setText("0")
			self.pushButton_0.setIconFile("")
			self.pushButton_0.setIconWidth(-1)
			self.pushButton_0.setIconHeight(-1)
			self.pushButton_0.setCheckable(false)
			self.pushButton_0.setCheck(false)
			self.gridLayout.addChild(self.pushButton_0, 4, 1)
			self.pushButton_Cancel=SPushButton(self.gridLayout)
			self.pushButton_Cancel.setX(83)
			self.pushButton_Cancel.setY(215)
			self.pushButton_Cancel.setWidth(73)
			self.pushButton_Cancel.setHeight(24)
			self.pushButton_Cancel.setEnable(true)
			self.pushButton_Cancel.setFontFamily("Gulim")
			self.pushButton_Cancel.setFontSize(9)
			self.pushButton_Cancel.setFontWeight(50)
			self.pushButton_Cancel.setFontItalic(false)
			self.pushButton_Cancel.setCursorShape(0)
			self.pushButton_Cancel.setText("Cancel")
			self.pushButton_Cancel.setIconFile("")
			self.pushButton_Cancel.setIconWidth(-1)
			self.pushButton_Cancel.setIconHeight(-1)
			self.pushButton_Cancel.setCheckable(false)
			self.pushButton_Cancel.setCheck(false)
			self.gridLayout.addChild(self.pushButton_Cancel, 5, 2)
			self.pushButton_OK=SPushButton(self.gridLayout)
			self.pushButton_OK.setX(166)
			self.pushButton_OK.setY(215)
			self.pushButton_OK.setWidth(73)
			self.pushButton_OK.setHeight(24)
			self.pushButton_OK.setEnable(true)
			self.pushButton_OK.setFontFamily("Gulim")
			self.pushButton_OK.setFontSize(9)
			self.pushButton_OK.setFontWeight(50)
			self.pushButton_OK.setFontItalic(false)
			self.pushButton_OK.setCursorShape(0)
			self.pushButton_OK.setText("OK")
			self.pushButton_OK.setIconFile("")
			self.pushButton_OK.setIconWidth(-1)
			self.pushButton_OK.setIconHeight(-1)
			self.pushButton_OK.setCheckable(false)
			self.pushButton_OK.setCheck(false)
			self.gridLayout.addChild(self.pushButton_OK, 5, 1)
			self.pushButton_7=SPushButton(self.gridLayout)
			self.pushButton_7.setX(0)
			self.pushButton_7.setY(181)
			self.pushButton_7.setWidth(73)
			self.pushButton_7.setHeight(24)
			self.pushButton_7.setEnable(true)
			self.pushButton_7.setFontFamily("Gulim")
			self.pushButton_7.setFontSize(9)
			self.pushButton_7.setFontWeight(50)
			self.pushButton_7.setFontItalic(false)
			self.pushButton_7.setCursorShape(0)
			self.pushButton_7.setText("7")
			self.pushButton_7.setIconFile("")
			self.pushButton_7.setIconWidth(-1)
			self.pushButton_7.setIconHeight(-1)
			self.pushButton_7.setCheckable(false)
			self.pushButton_7.setCheck(false)
			self.gridLayout.addChild(self.pushButton_7, 1, 0)
			self.pushButton_4=SPushButton(self.gridLayout)
			self.pushButton_4.setX(0)
			self.pushButton_4.setY(147)
			self.pushButton_4.setWidth(73)
			self.pushButton_4.setHeight(24)
			self.pushButton_4.setEnable(true)
			self.pushButton_4.setFontFamily("Gulim")
			self.pushButton_4.setFontSize(9)
			self.pushButton_4.setFontWeight(50)
			self.pushButton_4.setFontItalic(false)
			self.pushButton_4.setCursorShape(0)
			self.pushButton_4.setText("4")
			self.pushButton_4.setIconFile("")
			self.pushButton_4.setIconWidth(-1)
			self.pushButton_4.setIconHeight(-1)
			self.pushButton_4.setCheckable(false)
			self.pushButton_4.setCheck(false)
			self.gridLayout.addChild(self.pushButton_4, 2, 0)
			self.pushButton_1=SPushButton(self.gridLayout)
			self.pushButton_1.setX(0)
			self.pushButton_1.setY(112)
			self.pushButton_1.setWidth(73)
			self.pushButton_1.setHeight(24)
			self.pushButton_1.setEnable(true)
			self.pushButton_1.setFontFamily("Gulim")
			self.pushButton_1.setFontSize(9)
			self.pushButton_1.setFontWeight(50)
			self.pushButton_1.setFontItalic(false)
			self.pushButton_1.setCursorShape(0)
			self.pushButton_1.setText("1")
			self.pushButton_1.setIconFile("")
			self.pushButton_1.setIconWidth(-1)
			self.pushButton_1.setIconHeight(-1)
			self.pushButton_1.setCheckable(false)
			self.pushButton_1.setCheck(false)
			self.gridLayout.addChild(self.pushButton_1, 3, 0)
			self.pushButton_00=SPushButton(self.gridLayout)
			self.pushButton_00.setX(0)
			self.pushButton_00.setY(78)
			self.pushButton_00.setWidth(73)
			self.pushButton_00.setHeight(24)
			self.pushButton_00.setEnable(true)
			self.pushButton_00.setFontFamily("Gulim")
			self.pushButton_00.setFontSize(9)
			self.pushButton_00.setFontWeight(50)
			self.pushButton_00.setFontItalic(false)
			self.pushButton_00.setCursorShape(0)
			self.pushButton_00.setText("00")
			self.pushButton_00.setIconFile("")
			self.pushButton_00.setIconWidth(-1)
			self.pushButton_00.setIconHeight(-1)
			self.pushButton_00.setCheckable(false)
			self.pushButton_00.setCheck(false)
			self.gridLayout.addChild(self.pushButton_00, 4, 0)
			self.pushButton_8=SPushButton(self.gridLayout)
			self.pushButton_8.setX(83)
			self.pushButton_8.setY(181)
			self.pushButton_8.setWidth(73)
			self.pushButton_8.setHeight(24)
			self.pushButton_8.setEnable(true)
			self.pushButton_8.setFontFamily("Gulim")
			self.pushButton_8.setFontSize(9)
			self.pushButton_8.setFontWeight(50)
			self.pushButton_8.setFontItalic(false)
			self.pushButton_8.setCursorShape(0)
			self.pushButton_8.setText("8")
			self.pushButton_8.setIconFile("")
			self.pushButton_8.setIconWidth(-1)
			self.pushButton_8.setIconHeight(-1)
			self.pushButton_8.setCheckable(false)
			self.pushButton_8.setCheck(false)
			self.gridLayout.addChild(self.pushButton_8, 1, 1)
			self.pushButton_5=SPushButton(self.gridLayout)
			self.pushButton_5.setX(83)
			self.pushButton_5.setY(147)
			self.pushButton_5.setWidth(73)
			self.pushButton_5.setHeight(24)
			self.pushButton_5.setEnable(true)
			self.pushButton_5.setFontFamily("Gulim")
			self.pushButton_5.setFontSize(9)
			self.pushButton_5.setFontWeight(50)
			self.pushButton_5.setFontItalic(false)
			self.pushButton_5.setCursorShape(0)
			self.pushButton_5.setText("5")
			self.pushButton_5.setIconFile("")
			self.pushButton_5.setIconWidth(-1)
			self.pushButton_5.setIconHeight(-1)
			self.pushButton_5.setCheckable(false)
			self.pushButton_5.setCheck(false)
			self.gridLayout.addChild(self.pushButton_5, 2, 1)
			self.pushButton_9=SPushButton(self.gridLayout)
			self.pushButton_9.setX(166)
			self.pushButton_9.setY(181)
			self.pushButton_9.setWidth(73)
			self.pushButton_9.setHeight(24)
			self.pushButton_9.setEnable(true)
			self.pushButton_9.setFontFamily("Gulim")
			self.pushButton_9.setFontSize(9)
			self.pushButton_9.setFontWeight(50)
			self.pushButton_9.setFontItalic(false)
			self.pushButton_9.setCursorShape(0)
			self.pushButton_9.setText("9")
			self.pushButton_9.setIconFile("")
			self.pushButton_9.setIconWidth(-1)
			self.pushButton_9.setIconHeight(-1)
			self.pushButton_9.setCheckable(false)
			self.pushButton_9.setCheck(false)
			self.gridLayout.addChild(self.pushButton_9, 1, 2)
			self.pushButton_6=SPushButton(self.gridLayout)
			self.pushButton_6.setX(166)
			self.pushButton_6.setY(147)
			self.pushButton_6.setWidth(73)
			self.pushButton_6.setHeight(24)
			self.pushButton_6.setEnable(true)
			self.pushButton_6.setFontFamily("Gulim")
			self.pushButton_6.setFontSize(9)
			self.pushButton_6.setFontWeight(50)
			self.pushButton_6.setFontItalic(false)
			self.pushButton_6.setCursorShape(0)
			self.pushButton_6.setText("6")
			self.pushButton_6.setIconFile("")
			self.pushButton_6.setIconWidth(-1)
			self.pushButton_6.setIconHeight(-1)
			self.pushButton_6.setCheckable(false)
			self.pushButton_6.setCheck(false)
			self.gridLayout.addChild(self.pushButton_6, 2, 2)
			self.pushButton_3=SPushButton(self.gridLayout)
			self.pushButton_3.setX(166)
			self.pushButton_3.setY(112)
			self.pushButton_3.setWidth(73)
			self.pushButton_3.setHeight(24)
			self.pushButton_3.setEnable(true)
			self.pushButton_3.setFontFamily("Gulim")
			self.pushButton_3.setFontSize(9)
			self.pushButton_3.setFontWeight(50)
			self.pushButton_3.setFontItalic(false)
			self.pushButton_3.setCursorShape(0)
			self.pushButton_3.setText("3")
			self.pushButton_3.setIconFile("")
			self.pushButton_3.setIconWidth(-1)
			self.pushButton_3.setIconHeight(-1)
			self.pushButton_3.setCheckable(false)
			self.pushButton_3.setCheck(false)
			self.gridLayout.addChild(self.pushButton_3, 3, 2)
			self.pushButton_2=SPushButton(self.gridLayout)
			self.pushButton_2.setX(83)
			self.pushButton_2.setY(112)
			self.pushButton_2.setWidth(73)
			self.pushButton_2.setHeight(24)
			self.pushButton_2.setEnable(true)
			self.pushButton_2.setFontFamily("Gulim")
			self.pushButton_2.setFontSize(9)
			self.pushButton_2.setFontWeight(50)
			self.pushButton_2.setFontItalic(false)
			self.pushButton_2.setCursorShape(0)
			self.pushButton_2.setText("2")
			self.pushButton_2.setIconFile("")
			self.pushButton_2.setIconWidth(-1)
			self.pushButton_2.setIconHeight(-1)
			self.pushButton_2.setCheckable(false)
			self.pushButton_2.setCheck(false)
			self.gridLayout.addChild(self.pushButton_2, 3, 1)
			self.pushButton_clear=SPushButton(self.gridLayout)
			self.pushButton_clear.setX(83)
			self.pushButton_clear.setY(78)
			self.pushButton_clear.setWidth(73)
			self.pushButton_clear.setHeight(24)
			self.pushButton_clear.setEnable(true)
			self.pushButton_clear.setFontFamily("Gulim")
			self.pushButton_clear.setFontSize(9)
			self.pushButton_clear.setFontWeight(50)
			self.pushButton_clear.setFontItalic(false)
			self.pushButton_clear.setCursorShape(0)
			self.pushButton_clear.setText("Clear")
			self.pushButton_clear.setIconFile("")
			self.pushButton_clear.setIconWidth(-1)
			self.pushButton_clear.setIconHeight(-1)
			self.pushButton_clear.setCheckable(false)
			self.pushButton_clear.setCheck(false)
			self.gridLayout.addChild(self.pushButton_clear, 5, 0)
			self.pushButton_Back=SPushButton(self.gridLayout)
			self.pushButton_Back.setX(166)
			self.pushButton_Back.setY(78)
			self.pushButton_Back.setWidth(73)
			self.pushButton_Back.setHeight(24)
			self.pushButton_Back.setEnable(true)
			self.pushButton_Back.setFontFamily("Gulim")
			self.pushButton_Back.setFontSize(9)
			self.pushButton_Back.setFontWeight(50)
			self.pushButton_Back.setFontItalic(false)
			self.pushButton_Back.setCursorShape(0)
			self.pushButton_Back.setText("Back")
			self.pushButton_Back.setIconFile("")
			self.pushButton_Back.setIconWidth(-1)
			self.pushButton_Back.setIconHeight(-1)
			self.pushButton_Back.setCheckable(false)
			self.pushButton_Back.setCheck(false)
			self.gridLayout.addChild(self.pushButton_Back, 4, 2)
			self.pushButtonMin=SPushButton(self.gridLayout)
			self.pushButtonMin.setX(0)
			self.pushButtonMin.setY(10)
			self.pushButtonMin.setWidth(73)
			self.pushButtonMin.setHeight(24)
			self.pushButtonMin.setEnable(true)
			self.pushButtonMin.setFontFamily("Gulim")
			self.pushButtonMin.setFontSize(9)
			self.pushButtonMin.setFontWeight(50)
			self.pushButtonMin.setFontItalic(false)
			self.pushButtonMin.setCursorShape(0)
			self.pushButtonMin.setText("Min")
			self.pushButtonMin.setIconFile("")
			self.pushButtonMin.setIconWidth(-1)
			self.pushButtonMin.setIconHeight(-1)
			self.pushButtonMin.setCheckable(false)
			self.pushButtonMin.setCheck(false)
			self.gridLayout.addChild(self.pushButtonMin, 0, 0)
			self.pushButtonMax=SPushButton(self.gridLayout)
			self.pushButtonMax.setX(0)
			self.pushButtonMax.setY(44)
			self.pushButtonMax.setWidth(73)
			self.pushButtonMax.setHeight(24)
			self.pushButtonMax.setEnable(true)
			self.pushButtonMax.setFontFamily("Gulim")
			self.pushButtonMax.setFontSize(9)
			self.pushButtonMax.setFontWeight(50)
			self.pushButtonMax.setFontItalic(false)
			self.pushButtonMax.setCursorShape(0)
			self.pushButtonMax.setText("Max")
			self.pushButtonMax.setIconFile("")
			self.pushButtonMax.setIconWidth(-1)
			self.pushButtonMax.setIconHeight(-1)
			self.pushButtonMax.setCheckable(false)
			self.pushButtonMax.setCheck(false)
			self.gridLayout.addChild(self.pushButtonMax, 0, 2)
			self.labelMin=SLabel(self.gridLayout)
			self.labelMin.setX(83)
			self.labelMin.setY(10)
			self.labelMin.setWidth(73)
			self.labelMin.setHeight(24)
			self.labelMin.setEnable(true)
			self.labelMin.setFontFamily("Gulim")
			self.labelMin.setFontSize(9)
			self.labelMin.setFontWeight(50)
			self.labelMin.setFontItalic(false)
			self.labelMin.setCursorShape(0)
			self.labelMin.setFrameShape(0)
			self.labelMin.setLineWidth(1)
			self.labelMin.setMidLineWidth(1)
			self.labelMin.setText("Min")
			self.labelMin.setHorizontalAlignment(1)
			self.labelMin.setVerticalAlignment(128)
			self.labelMin.setMargin(0)
			self.gridLayout.addChild(self.labelMin, 0, 1)
			self.labelMax=SLabel(self.gridLayout)
			self.labelMax.setX(83)
			self.labelMax.setY(44)
			self.labelMax.setWidth(73)
			self.labelMax.setHeight(24)
			self.labelMax.setEnable(true)
			self.labelMax.setFontFamily("Gulim")
			self.labelMax.setFontSize(9)
			self.labelMax.setFontWeight(50)
			self.labelMax.setFontItalic(false)
			self.labelMax.setCursorShape(0)
			self.labelMax.setFrameShape(0)
			self.labelMax.setLineWidth(1)
			self.labelMax.setMidLineWidth(1)
			self.labelMax.setText("Max")
			self.labelMax.setHorizontalAlignment(1)
			self.labelMax.setVerticalAlignment(128)
			self.labelMax.setMargin(0)
			self.gridLayout.addChild(self.labelMax, 0, 3)
			self.pushButton_dot=SPushButton(self.gridLayout)
			self.pushButton_dot.setX(0)
			self.pushButton_dot.setY(215)
			self.pushButton_dot.setWidth(73)
			self.pushButton_dot.setHeight(24)
			self.pushButton_dot.setEnable(true)
			self.pushButton_dot.setFontFamily("Gulim")
			self.pushButton_dot.setFontSize(9)
			self.pushButton_dot.setFontWeight(50)
			self.pushButton_dot.setFontItalic(false)
			self.pushButton_dot.setCursorShape(0)
			self.pushButton_dot.setText(".")
			self.pushButton_dot.setIconFile("")
			self.pushButton_dot.setIconWidth(-1)
			self.pushButton_dot.setIconHeight(-1)
			self.pushButton_dot.setCheckable(false)
			self.pushButton_dot.setCheck(false)
			self.gridLayout.addChild(self.pushButton_dot, 1, 3)
            
            self.labelMin.setText(str(self.min))
            self.labelMax.setText(str(self.max))
            self.lineEdit.setText(format(float(self.textNoFormat), ",f"))

			self.pushButton_0.clicked.connect(self.slotClickedPushButton_0)

			self.pushButton_Cancel.clicked.connect(self.slotClickedPushButton_Cancel)

			self.pushButton_OK.clicked.connect(self.slotClickedPushButton_OK)

			self.pushButton_7.clicked.connect(self.slotClickedPushButton_7)

			self.pushButton_4.clicked.connect(self.slotClickedPushButton_4)

			self.pushButton_1.clicked.connect(self.slotClickedPushButton_1)

			self.pushButton_00.clicked.connect(self.slotClickedPushButton_00)

			self.pushButton_8.clicked.connect(self.slotClickedPushButton_8)

			self.pushButton_5.clicked.connect(self.slotClickedPushButton_5)

			self.pushButton_9.clicked.connect(self.slotClickedPushButton_9)

			self.pushButton_6.clicked.connect(self.slotClickedPushButton_6)

			self.pushButton_3.clicked.connect(self.slotClickedPushButton_3)

			self.pushButton_2.clicked.connect(self.slotClickedPushButton_2)

			self.pushButton_clear.clicked.connect(self.slotClickedPushButton_clear)

			self.pushButton_Back.clicked.connect(self.slotClickedPushButton_Back)

			self.pushButton_dot.clicked.connect(self.slotClickedPushButton_dot)

            self.lineEdit.keyPress.connect(self.slotKeyPress)
		}

        def updateNumber(self, numberText : str)
        {
            if(self.firstInput)
            {
               self.textNoFormat = numberText
               self.firstInput = false;
            }
            else
            {
               self.textNoFormat.append(numberText)
            }

            formatedText = self.textNoFormat

            if(formatedText == "0.0")
            {
                self.textNoFormat = "0.0"
            }

            self.lineEdit.setText(formatedText)
        }

		def slotClickedPushButton_14(self, checked){}

		def slotClickedPushButton_00(self, checked){
            self.updateNumber("00")
        }

        def _clear(self)
        {
            self.lineEdit.setText("0.0")
            self.textNoFormat = ""
        }

		def slotClickedPushButton_clear(self, checked){
            self._clear()
        }

        def _back(self)
        {
            n = len(self.textNoFormat)

            if(n > 0)
            {
                self.textNoFormat = self.textNoFormat.substr(0, n - 1)
                self.lineEdit.setText(self.textNoFormat)
            }
        }

		def _dot(self)
		{
			self.updateNumber(".")
		}

		def slotClickedPushButton_Back(self, checked){
            self._back()
        }

		def slotClickedPushButton_1(self, checked){
            self.updateNumber(str(1))
		}

		def slotClickedPushButton_2(self, checked){
            self.updateNumber(str(2))
        }

		def slotClickedPushButton_3(self, checked){
            self.updateNumber(str(3))
        }

		def slotClickedPushButton_4(self, checked){
            self.updateNumber(str(4))
        }

		def slotClickedPushButton_5(self, checked){
            self.updateNumber(str(5))
        }

		def slotClickedPushButton_6(self, checked){
            self.updateNumber(str(6))
        }

		def slotClickedPushButton_7(self, checked){
            self.updateNumber(str(7))
        }

		def slotClickedPushButton_8(self, checked){
            self.updateNumber(str(8))
        }

		def slotClickedPushButton_9(self, checked){
            self.updateNumber(str(9))
        }

		def slotClickedPushButton_0(self, checked){
            self.updateNumber(str(0))
        }

		def slotClickedPushButton_dot(self, checked){
            self.updateNumber(str("."))
        }

		def slotClickedPushButton_Cancel(self, checked){
            self.onCancel.emit(float(self.textNoFormat))
            self.onCancelWithSender.emit(0)
            self.reject()
        }

		def slotClickedPushButton_OK(self, checked){
            number = float(self.textNoFormat)

            if(number >= self.min)
            {
                if(number <= self.max)
                {
                    self.onOk.emit(float(self.textNoFormat))
                    self.onOkWithSender.emit(float(self.textNoFormat))
                    self.done(1)
                }
                else
                {
                    msgBox = SMessageBox(self)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("The number is larger than max value")
                    msgBox.exec()
                }
            }
            else
            {
                msgBox = SMessageBox(self)
                msgBox.setWindowTitle("Error")
                msgBox.setText("The number is lower than min value")
                msgBox.exec()
            }
        }

        def slotKeyPress(self, key)
        {
			if(key == 45)
			{
				self.updateNumber("-")
			}
            if(key >= 48)
            {
                if(key <= 57)
                {
                    self.updateNumber(str(key - 48))

                }
            }

			if(key == 46) #dot
			{
				self._dot()
			}

            if(key == 16777219) #backspace
            {
                self._back()
            }

            if(key == 16777216) #escape
            {
                self._clear()
            }

            print(key)
        }
        def getMin(self)
        {
            return 10.0
        }
}


class SNumpad(SDialog)
{

		def __init__(self, parent: SWidget, min: int, max: int, default: float)
		{
			self.min=min
			self.max=max
			self.default=default

            self.onCancel = Signal()
            self.onCancelWithSender = Signal()
            self.onOk = Signal()
            self.onOkWithSender = Signal()
            self.textNoFormat = str(self.default)

            self.firstInput = true

			self.setX(0)
			self.setY(0)
			self.setWidth(274)
			self.setHeight(333)
			self.setEnable(true)
			self.setFontFamily("Gulim")
			self.setFontSize(9)
			self.setFontWeight(50)
			self.setFontItalic(false)
			self.setCursorShape(0)
			self.setWindowTitle("Numpad")
			self.verticalLayout=SVerticalLayout(self)
			self.verticalLayout.setX(6)
			self.verticalLayout.setY(6)
			self.verticalLayout.setWidth(259)
			self.verticalLayout.setHeight(320)
			self.verticalLayout.setEnable(true)
			self.verticalLayout.setFontFamily("Gulim")
			self.verticalLayout.setFontSize(9)
			self.verticalLayout.setFontWeight(50)
			self.verticalLayout.setFontItalic(false)
			self.verticalLayout.setCursorShape(0)
			self.verticalLayout.setMarginLeft(10)
			self.verticalLayout.setMarginTop(10)
			self.verticalLayout.setMarginRight(10)
			self.verticalLayout.setMarginBottom(10)
			self.verticalLayout.setLayoutSpacing(0)
			self.verticalLayout.setLayoutStretch([1,5])
			self.lineEdit=SLineEdit(self.verticalLayout)
			self.lineEdit.setX(10)
			self.lineEdit.setY(10)
			self.lineEdit.setWidth(239)
			self.lineEdit.setHeight(50)
			self.lineEdit.setEnable(true)
			self.lineEdit.setFontFamily("Gulim")
			self.lineEdit.setFontSize(9)
			self.lineEdit.setFontWeight(50)
			self.lineEdit.setFontItalic(false)
			self.lineEdit.setCursorShape(0)
			self.lineEdit.setText("")
			self.lineEdit.setReadOnly(true)
			self.lineEdit.setAlignment(2)

			self.verticalLayout.addChild(self.lineEdit)
			self.gridLayout=SGridLayout(self.verticalLayout)
			self.gridLayout.setX(10)
			self.gridLayout.setY(60)
			self.gridLayout.setWidth(239)
			self.gridLayout.setHeight(250)
			self.gridLayout.setEnable(true)
			self.gridLayout.setFontFamily("Gulim")
			self.gridLayout.setFontSize(9)
			self.gridLayout.setFontWeight(50)
			self.gridLayout.setFontItalic(false)
			self.gridLayout.setCursorShape(0)
			self.gridLayout.setMarginLeft(0)
			self.gridLayout.setMarginTop(10)
			self.gridLayout.setMarginRight(0)
			self.gridLayout.setMarginBottom(10)
			self.gridLayout.setVerticalSpacing(10)
			self.gridLayout.setHorizontalSpacing(10)
			self.gridLayout.setVerticalStretch([0,0,0,0,0,0,0])
			self.gridLayout.setHorizontalStretch([0,0,0])
			self.gridLayout.setIndexMapping([18,19,20,15,12,9,6,16,13,17,14,11,10,7,8,0,3,1,4])
			self.gridLayout.setRow(4)
			self.gridLayout.setColumn(6)
			self.verticalLayout.addChild(self.gridLayout)
			self.pushButton_0=SPushButton(self.gridLayout)
			self.pushButton_0.setX(0)
			self.pushButton_0.setY(215)
			self.pushButton_0.setWidth(73)
			self.pushButton_0.setHeight(24)
			self.pushButton_0.setEnable(true)
			self.pushButton_0.setFontFamily("Gulim")
			self.pushButton_0.setFontSize(9)
			self.pushButton_0.setFontWeight(50)
			self.pushButton_0.setFontItalic(false)
			self.pushButton_0.setCursorShape(0)
			self.pushButton_0.setText("0")
			self.pushButton_0.setIconFile("")
			self.pushButton_0.setIconWidth(-1)
			self.pushButton_0.setIconHeight(-1)
			self.pushButton_0.setCheckable(false)
			self.pushButton_0.setCheck(false)
			self.gridLayout.addChild(self.pushButton_0, 4, 1)
			self.pushButton_Cancel=SPushButton(self.gridLayout)
			self.pushButton_Cancel.setX(83)
			self.pushButton_Cancel.setY(215)
			self.pushButton_Cancel.setWidth(73)
			self.pushButton_Cancel.setHeight(24)
			self.pushButton_Cancel.setEnable(true)
			self.pushButton_Cancel.setFontFamily("Gulim")
			self.pushButton_Cancel.setFontSize(9)
			self.pushButton_Cancel.setFontWeight(50)
			self.pushButton_Cancel.setFontItalic(false)
			self.pushButton_Cancel.setCursorShape(0)
			self.pushButton_Cancel.setText("Cancel")
			self.pushButton_Cancel.setIconFile("")
			self.pushButton_Cancel.setIconWidth(-1)
			self.pushButton_Cancel.setIconHeight(-1)
			self.pushButton_Cancel.setCheckable(false)
			self.pushButton_Cancel.setCheck(false)
			self.gridLayout.addChild(self.pushButton_Cancel, 5, 2)
			self.pushButton_OK=SPushButton(self.gridLayout)
			self.pushButton_OK.setX(166)
			self.pushButton_OK.setY(215)
			self.pushButton_OK.setWidth(73)
			self.pushButton_OK.setHeight(24)
			self.pushButton_OK.setEnable(true)
			self.pushButton_OK.setFontFamily("Gulim")
			self.pushButton_OK.setFontSize(9)
			self.pushButton_OK.setFontWeight(50)
			self.pushButton_OK.setFontItalic(false)
			self.pushButton_OK.setCursorShape(0)
			self.pushButton_OK.setText("OK")
			self.pushButton_OK.setIconFile("")
			self.pushButton_OK.setIconWidth(-1)
			self.pushButton_OK.setIconHeight(-1)
			self.pushButton_OK.setCheckable(false)
			self.pushButton_OK.setCheck(false)
			self.gridLayout.addChild(self.pushButton_OK, 5, 1)
			self.pushButton_7=SPushButton(self.gridLayout)
			self.pushButton_7.setX(0)
			self.pushButton_7.setY(181)
			self.pushButton_7.setWidth(73)
			self.pushButton_7.setHeight(24)
			self.pushButton_7.setEnable(true)
			self.pushButton_7.setFontFamily("Gulim")
			self.pushButton_7.setFontSize(9)
			self.pushButton_7.setFontWeight(50)
			self.pushButton_7.setFontItalic(false)
			self.pushButton_7.setCursorShape(0)
			self.pushButton_7.setText("7")
			self.pushButton_7.setIconFile("")
			self.pushButton_7.setIconWidth(-1)
			self.pushButton_7.setIconHeight(-1)
			self.pushButton_7.setCheckable(false)
			self.pushButton_7.setCheck(false)
			self.gridLayout.addChild(self.pushButton_7, 1, 0)
			self.pushButton_4=SPushButton(self.gridLayout)
			self.pushButton_4.setX(0)
			self.pushButton_4.setY(147)
			self.pushButton_4.setWidth(73)
			self.pushButton_4.setHeight(24)
			self.pushButton_4.setEnable(true)
			self.pushButton_4.setFontFamily("Gulim")
			self.pushButton_4.setFontSize(9)
			self.pushButton_4.setFontWeight(50)
			self.pushButton_4.setFontItalic(false)
			self.pushButton_4.setCursorShape(0)
			self.pushButton_4.setText("4")
			self.pushButton_4.setIconFile("")
			self.pushButton_4.setIconWidth(-1)
			self.pushButton_4.setIconHeight(-1)
			self.pushButton_4.setCheckable(false)
			self.pushButton_4.setCheck(false)
			self.gridLayout.addChild(self.pushButton_4, 2, 0)
			self.pushButton_1=SPushButton(self.gridLayout)
			self.pushButton_1.setX(0)
			self.pushButton_1.setY(112)
			self.pushButton_1.setWidth(73)
			self.pushButton_1.setHeight(24)
			self.pushButton_1.setEnable(true)
			self.pushButton_1.setFontFamily("Gulim")
			self.pushButton_1.setFontSize(9)
			self.pushButton_1.setFontWeight(50)
			self.pushButton_1.setFontItalic(false)
			self.pushButton_1.setCursorShape(0)
			self.pushButton_1.setText("1")
			self.pushButton_1.setIconFile("")
			self.pushButton_1.setIconWidth(-1)
			self.pushButton_1.setIconHeight(-1)
			self.pushButton_1.setCheckable(false)
			self.pushButton_1.setCheck(false)
			self.gridLayout.addChild(self.pushButton_1, 3, 0)
			self.pushButton_00=SPushButton(self.gridLayout)
			self.pushButton_00.setX(0)
			self.pushButton_00.setY(78)
			self.pushButton_00.setWidth(73)
			self.pushButton_00.setHeight(24)
			self.pushButton_00.setEnable(true)
			self.pushButton_00.setFontFamily("Gulim")
			self.pushButton_00.setFontSize(9)
			self.pushButton_00.setFontWeight(50)
			self.pushButton_00.setFontItalic(false)
			self.pushButton_00.setCursorShape(0)
			self.pushButton_00.setText("00")
			self.pushButton_00.setIconFile("")
			self.pushButton_00.setIconWidth(-1)
			self.pushButton_00.setIconHeight(-1)
			self.pushButton_00.setCheckable(false)
			self.pushButton_00.setCheck(false)
			self.gridLayout.addChild(self.pushButton_00, 4, 0)
			self.pushButton_8=SPushButton(self.gridLayout)
			self.pushButton_8.setX(83)
			self.pushButton_8.setY(181)
			self.pushButton_8.setWidth(73)
			self.pushButton_8.setHeight(24)
			self.pushButton_8.setEnable(true)
			self.pushButton_8.setFontFamily("Gulim")
			self.pushButton_8.setFontSize(9)
			self.pushButton_8.setFontWeight(50)
			self.pushButton_8.setFontItalic(false)
			self.pushButton_8.setCursorShape(0)
			self.pushButton_8.setText("8")
			self.pushButton_8.setIconFile("")
			self.pushButton_8.setIconWidth(-1)
			self.pushButton_8.setIconHeight(-1)
			self.pushButton_8.setCheckable(false)
			self.pushButton_8.setCheck(false)
			self.gridLayout.addChild(self.pushButton_8, 1, 1)
			self.pushButton_5=SPushButton(self.gridLayout)
			self.pushButton_5.setX(83)
			self.pushButton_5.setY(147)
			self.pushButton_5.setWidth(73)
			self.pushButton_5.setHeight(24)
			self.pushButton_5.setEnable(true)
			self.pushButton_5.setFontFamily("Gulim")
			self.pushButton_5.setFontSize(9)
			self.pushButton_5.setFontWeight(50)
			self.pushButton_5.setFontItalic(false)
			self.pushButton_5.setCursorShape(0)
			self.pushButton_5.setText("5")
			self.pushButton_5.setIconFile("")
			self.pushButton_5.setIconWidth(-1)
			self.pushButton_5.setIconHeight(-1)
			self.pushButton_5.setCheckable(false)
			self.pushButton_5.setCheck(false)
			self.gridLayout.addChild(self.pushButton_5, 2, 1)
			self.pushButton_9=SPushButton(self.gridLayout)
			self.pushButton_9.setX(166)
			self.pushButton_9.setY(181)
			self.pushButton_9.setWidth(73)
			self.pushButton_9.setHeight(24)
			self.pushButton_9.setEnable(true)
			self.pushButton_9.setFontFamily("Gulim")
			self.pushButton_9.setFontSize(9)
			self.pushButton_9.setFontWeight(50)
			self.pushButton_9.setFontItalic(false)
			self.pushButton_9.setCursorShape(0)
			self.pushButton_9.setText("9")
			self.pushButton_9.setIconFile("")
			self.pushButton_9.setIconWidth(-1)
			self.pushButton_9.setIconHeight(-1)
			self.pushButton_9.setCheckable(false)
			self.pushButton_9.setCheck(false)
			self.gridLayout.addChild(self.pushButton_9, 1, 2)
			self.pushButton_6=SPushButton(self.gridLayout)
			self.pushButton_6.setX(166)
			self.pushButton_6.setY(147)
			self.pushButton_6.setWidth(73)
			self.pushButton_6.setHeight(24)
			self.pushButton_6.setEnable(true)
			self.pushButton_6.setFontFamily("Gulim")
			self.pushButton_6.setFontSize(9)
			self.pushButton_6.setFontWeight(50)
			self.pushButton_6.setFontItalic(false)
			self.pushButton_6.setCursorShape(0)
			self.pushButton_6.setText("6")
			self.pushButton_6.setIconFile("")
			self.pushButton_6.setIconWidth(-1)
			self.pushButton_6.setIconHeight(-1)
			self.pushButton_6.setCheckable(false)
			self.pushButton_6.setCheck(false)
			self.gridLayout.addChild(self.pushButton_6, 2, 2)
			self.pushButton_3=SPushButton(self.gridLayout)
			self.pushButton_3.setX(166)
			self.pushButton_3.setY(112)
			self.pushButton_3.setWidth(73)
			self.pushButton_3.setHeight(24)
			self.pushButton_3.setEnable(true)
			self.pushButton_3.setFontFamily("Gulim")
			self.pushButton_3.setFontSize(9)
			self.pushButton_3.setFontWeight(50)
			self.pushButton_3.setFontItalic(false)
			self.pushButton_3.setCursorShape(0)
			self.pushButton_3.setText("3")
			self.pushButton_3.setIconFile("")
			self.pushButton_3.setIconWidth(-1)
			self.pushButton_3.setIconHeight(-1)
			self.pushButton_3.setCheckable(false)
			self.pushButton_3.setCheck(false)
			self.gridLayout.addChild(self.pushButton_3, 3, 2)
			self.pushButton_2=SPushButton(self.gridLayout)
			self.pushButton_2.setX(83)
			self.pushButton_2.setY(112)
			self.pushButton_2.setWidth(73)
			self.pushButton_2.setHeight(24)
			self.pushButton_2.setEnable(true)
			self.pushButton_2.setFontFamily("Gulim")
			self.pushButton_2.setFontSize(9)
			self.pushButton_2.setFontWeight(50)
			self.pushButton_2.setFontItalic(false)
			self.pushButton_2.setCursorShape(0)
			self.pushButton_2.setText("2")
			self.pushButton_2.setIconFile("")
			self.pushButton_2.setIconWidth(-1)
			self.pushButton_2.setIconHeight(-1)
			self.pushButton_2.setCheckable(false)
			self.pushButton_2.setCheck(false)
			self.gridLayout.addChild(self.pushButton_2, 3, 1)
			self.pushButton_clear=SPushButton(self.gridLayout)
			self.pushButton_clear.setX(83)
			self.pushButton_clear.setY(78)
			self.pushButton_clear.setWidth(73)
			self.pushButton_clear.setHeight(24)
			self.pushButton_clear.setEnable(true)
			self.pushButton_clear.setFontFamily("Gulim")
			self.pushButton_clear.setFontSize(9)
			self.pushButton_clear.setFontWeight(50)
			self.pushButton_clear.setFontItalic(false)
			self.pushButton_clear.setCursorShape(0)
			self.pushButton_clear.setText("Clear")
			self.pushButton_clear.setIconFile("")
			self.pushButton_clear.setIconWidth(-1)
			self.pushButton_clear.setIconHeight(-1)
			self.pushButton_clear.setCheckable(false)
			self.pushButton_clear.setCheck(false)
			self.gridLayout.addChild(self.pushButton_clear, 5, 0)
			self.pushButton_Back=SPushButton(self.gridLayout)
			self.pushButton_Back.setX(166)
			self.pushButton_Back.setY(78)
			self.pushButton_Back.setWidth(73)
			self.pushButton_Back.setHeight(24)
			self.pushButton_Back.setEnable(true)
			self.pushButton_Back.setFontFamily("Gulim")
			self.pushButton_Back.setFontSize(9)
			self.pushButton_Back.setFontWeight(50)
			self.pushButton_Back.setFontItalic(false)
			self.pushButton_Back.setCursorShape(0)
			self.pushButton_Back.setText("Back")
			self.pushButton_Back.setIconFile("")
			self.pushButton_Back.setIconWidth(-1)
			self.pushButton_Back.setIconHeight(-1)
			self.pushButton_Back.setCheckable(false)
			self.pushButton_Back.setCheck(false)
			self.gridLayout.addChild(self.pushButton_Back, 4, 2)
			self.pushButtonMin=SPushButton(self.gridLayout)
			self.pushButtonMin.setX(0)
			self.pushButtonMin.setY(10)
			self.pushButtonMin.setWidth(73)
			self.pushButtonMin.setHeight(24)
			self.pushButtonMin.setEnable(true)
			self.pushButtonMin.setFontFamily("Gulim")
			self.pushButtonMin.setFontSize(9)
			self.pushButtonMin.setFontWeight(50)
			self.pushButtonMin.setFontItalic(false)
			self.pushButtonMin.setCursorShape(0)
			self.pushButtonMin.setText("Min")
			self.pushButtonMin.setIconFile("")
			self.pushButtonMin.setIconWidth(-1)
			self.pushButtonMin.setIconHeight(-1)
			self.pushButtonMin.setCheckable(false)
			self.pushButtonMin.setCheck(false)
			self.gridLayout.addChild(self.pushButtonMin, 0, 0)
			self.pushButtonMax=SPushButton(self.gridLayout)
			self.pushButtonMax.setX(0)
			self.pushButtonMax.setY(44)
			self.pushButtonMax.setWidth(73)
			self.pushButtonMax.setHeight(24)
			self.pushButtonMax.setEnable(true)
			self.pushButtonMax.setFontFamily("Gulim")
			self.pushButtonMax.setFontSize(9)
			self.pushButtonMax.setFontWeight(50)
			self.pushButtonMax.setFontItalic(false)
			self.pushButtonMax.setCursorShape(0)
			self.pushButtonMax.setText("Max")
			self.pushButtonMax.setIconFile("")
			self.pushButtonMax.setIconWidth(-1)
			self.pushButtonMax.setIconHeight(-1)
			self.pushButtonMax.setCheckable(false)
			self.pushButtonMax.setCheck(false)
			self.gridLayout.addChild(self.pushButtonMax, 0, 2)
			self.labelMin=SLabel(self.gridLayout)
			self.labelMin.setX(83)
			self.labelMin.setY(10)
			self.labelMin.setWidth(73)
			self.labelMin.setHeight(24)
			self.labelMin.setEnable(true)
			self.labelMin.setFontFamily("Gulim")
			self.labelMin.setFontSize(9)
			self.labelMin.setFontWeight(50)
			self.labelMin.setFontItalic(false)
			self.labelMin.setCursorShape(0)
			self.labelMin.setFrameShape(0)
			self.labelMin.setLineWidth(1)
			self.labelMin.setMidLineWidth(1)
			self.labelMin.setText("Min")
			self.labelMin.setHorizontalAlignment(1)
			self.labelMin.setVerticalAlignment(128)
			self.labelMin.setMargin(0)
			self.gridLayout.addChild(self.labelMin, 0, 1)
			self.labelMax=SLabel(self.gridLayout)
			self.labelMax.setX(83)
			self.labelMax.setY(44)
			self.labelMax.setWidth(73)
			self.labelMax.setHeight(24)
			self.labelMax.setEnable(true)
			self.labelMax.setFontFamily("Gulim")
			self.labelMax.setFontSize(9)
			self.labelMax.setFontWeight(50)
			self.labelMax.setFontItalic(false)
			self.labelMax.setCursorShape(0)
			self.labelMax.setFrameShape(0)
			self.labelMax.setLineWidth(1)
			self.labelMax.setMidLineWidth(1)
			self.labelMax.setText("Max")
			self.labelMax.setHorizontalAlignment(1)
			self.labelMax.setVerticalAlignment(128)
			self.labelMax.setMargin(0)
			self.gridLayout.addChild(self.labelMax, 0, 3)

            self.labelMin.setText(str(self.min))
            self.labelMax.setText(str(self.max))
            self.lineEdit.setText(format(int(self.textNoFormat), ",d"))

			self.pushButton_0.clicked.connect(self.slotClickedPushButton_0)

			self.pushButton_Cancel.clicked.connect(self.slotClickedPushButton_Cancel)

			self.pushButton_OK.clicked.connect(self.slotClickedPushButton_OK)

			self.pushButton_7.clicked.connect(self.slotClickedPushButton_7)

			self.pushButton_4.clicked.connect(self.slotClickedPushButton_4)

			self.pushButton_1.clicked.connect(self.slotClickedPushButton_1)

			self.pushButton_00.clicked.connect(self.slotClickedPushButton_00)

			self.pushButton_8.clicked.connect(self.slotClickedPushButton_8)

			self.pushButton_5.clicked.connect(self.slotClickedPushButton_5)

			self.pushButton_9.clicked.connect(self.slotClickedPushButton_9)

			self.pushButton_6.clicked.connect(self.slotClickedPushButton_6)

			self.pushButton_3.clicked.connect(self.slotClickedPushButton_3)

			self.pushButton_2.clicked.connect(self.slotClickedPushButton_2)

			self.pushButton_clear.clicked.connect(self.slotClickedPushButton_clear)

			self.pushButton_Back.clicked.connect(self.slotClickedPushButton_Back)
            self.lineEdit.keyPress.connect(self.slotKeyPress)
			
			self.useRange = true
		}
		
		def setUseRange(self, use: bool)
		{
			self.useRange = use
			
			if(use == false)
			{
				self.pushButtonMax.setVisible(false)
				self.labelMax.setVisible(false)
				
				self.pushButtonMin.setVisible(false)
				self.labelMin.setVisible(false)
			}
		}

        def updateNumber(self, numberText : str)
        {
            if(self.firstInput)
            {
               self.textNoFormat = numberText
               self.firstInput = false;
            }
            else
            {
               self.textNoFormat.append(numberText)
            }

            formatedText = self.textNoFormat

            if(formatedText == "0")
            {
                self.textNoFormat = "0"
            }

            self.lineEdit.setText(formatedText)
        }

		def slotClickedPushButton_14(self, checked){}

		def slotClickedPushButton_00(self, checked){
            self.updateNumber("00")
        }

        def _clear(self)
        {
            self.lineEdit.setText("0")
            self.textNoFormat = ""
        }

		def slotClickedPushButton_clear(self, checked){
            self._clear()
        }

        def _back(self)
        {
            n = len(self.textNoFormat)

            if(n > 0)
            {
                self.textNoFormat = self.textNoFormat.substr(0, n - 1)
                self.lineEdit.setText(format(int(self.textNoFormat), ",d"))
            }
        }

		def slotClickedPushButton_Back(self, checked){
            self._back()
        }

		def slotClickedPushButton_1(self, checked){
            self.updateNumber(str(1))
		}

		def slotClickedPushButton_2(self, checked){
            self.updateNumber(str(2))
        }

		def slotClickedPushButton_3(self, checked){
            self.updateNumber(str(3))
        }

		def slotClickedPushButton_4(self, checked){
            self.updateNumber(str(4))
        }

		def slotClickedPushButton_5(self, checked){
            self.updateNumber(str(5))
        }

		def slotClickedPushButton_6(self, checked){
            self.updateNumber(str(6))
        }

		def slotClickedPushButton_7(self, checked){
            self.updateNumber(str(7))
        }

		def slotClickedPushButton_8(self, checked){
            self.updateNumber(str(8))
        }

		def slotClickedPushButton_9(self, checked){
            self.updateNumber(str(9))
        }

		def slotClickedPushButton_0(self, checked){
            self.updateNumber(str(0))
        }

		def slotClickedPushButton_Cancel(self, checked){
            self.onCancel.emit(int(self.textNoFormat))
            self.onCancelWithSender.emit(0)
            self.reject()
        }

		def slotClickedPushButton_OK(self, checked)
		{
            number = int(self.textNoFormat)
			
			if(self.useRange == false)
			{
				self.onOk.emit(int(self.textNoFormat))
				self.onOkWithSender.emit(int(self.textNoFormat))
				self.done(1)
			}
			else
			{
				if(number >= self.min)
				{
					if(number <= self.max)
					{
						self.onOk.emit(int(self.textNoFormat))
						self.onOkWithSender.emit(int(self.textNoFormat))
						self.done(1)
					}
					else
					{
						msgBox = SMessageBox(self)
						msgBox.setWindowTitle("Error")
						msgBox.setText("The number is larger than max value")
						msgBox.exec()
					}
				}
				else
				{
					msgBox = SMessageBox(self)
					msgBox.setWindowTitle("Error")
					msgBox.setText("The number is lower than min value")
					msgBox.exec()
				}
			}
        }

        def slotKeyPress(self, key)
        {
			if(key == 45)
			{
				self.updateNumber("-")
			}
            if(key >= 48)
            {
                if(key <= 57)
                {
                    self.updateNumber(str(key - 48))

                }
            }

            if(key == 16777219) #backspace
            {
                self._back()
            }

            if(key == 16777216) #escape
            {
                self._clear()
            }
        }
        def getMin(self)
        {
            return 10
        }
}

class SInputDialog(SDialog)
{
	def setLabelText(self, text: str){}
	def setTextValue(self, text: str){}
	def setInputMode(self, mode: int){}
	def textValue(self) -> str{}
	def intValue(self){}
}

class SMenu(SWidget)
{
	def __init__(self, parent : SWidget)
	{
		self.aboutToHide = Signal()
		self.aboutToShow = Signal()
		self.hovered = Signal()
		self.triggered = Signal()
	}
	def addAction(self, name : str)
	{}
	def popup(self, pos : SPointF)
	{}
	def addMenu(self, Menu : str)
	{}
	def addSeparator(self)
	{}
	def clear(self)
	{}
	def isEmpty(self) -> bool
	{}
	def setToolTipsVisible(self, b : bool)
	{}
	def title(self) -> str
	{}
	def toolTipsVisible(self) -> bool
	{}

}


class STextEdit()
{
	def setUndoRedoEnable(self, enable: bool){}
	def setReadOnly(self, ro: bool){}
	def setPlainText(self, text : str){}
	def acceptRichText(self) -> bool
	{}
	def anchorAt(self, pos : SPoint) -> str
	{}
	def canPaste(self) -> bool
	{}
	def ensureCursorVisible(self)
	{}
	def fontFamily(self) -> str
	{}
	def fontItalic(self) -> bool
	{}
	def fontUnderline(self) -> bool
	{}
	def fontWeight(self) -> int
	{}
	def isReadOnly(self) -> bool
	{}
	def isUndoRedoEnabled(self) -> bool
	{}
	def lineWrapColumnOrWidth(self) -> int
	{}
	def overwriteMode(self)
	{}
	def placeholderText(self) -> str
	{}
	def setAcceptRichText(self, accept : bool)
	{}
	def setDocumentTitle(self, title : str) -> str
	{}
	def setLineWrapColumnOrWidth(self, w : int) -> int
	{}
	def setOverwriteMode(self, overwrite : bool)
	{}
	def setPlaceholderText(self, placeholderText : str)
	{}
	def setTabChangesFocus(self, b : bool)
	{}
	def tabChangesFocus(self) -> bool
	{}
	def toHtml(self) -> str
	{}
	def toPlainText(self) -> str
	{}
	def append(self, text : str)
	{}
	def clear(self)
	{}
	def copy(self)
	{}
	def cut(self)
	{}
	def insertHtml(self, text : str)
	{}
	def insertPlainText(self, text : str)
	{}
	def paste(self)
	{}
	def redo(self)
	{}
	def scrollToAnchor(self, name : str)
	{}
	def selectAll(self)
	{}
	def setFontFamily(self, fontFamily : str)
	{}
	def setFontItalic(self, italic : bool)
	{}
	def setFontUnderline(self, underline : bool)
	{}
	def setFontWeight(self, weight : int)
	{}
	def setHtml(self, text : str)
	{}
	def setText(self, text : str)
	{}
	def undo(self)
	{}
}

class SAbstractSpinBox(SWidget)
{
	def setAlignment(self, flag : int)
	{}
	def setReadOnly(self, r : bool)
	{}
	def setFrame(self, enable : bool)
	{}
}

class SSpinBox(SAbstractSpinBox)
{
	def setMin(self, min: int)
	{}
	def setMax(self, max: int)
	{}
	def setSingleStep(self, val: int)
	{}
	def value(self) -> int
	{}
	def setPrefix(self, prefix : str)
	{}
	def setDisplayIntegerBase(self, base : int)
	{}
	def setSuffix(self, suffix : str)
	{}
}

class Unit()
{
	def config(self)
	{
		pass
	}

	def __init__(self)
	{
		self.children = list()
		pass
	}

	def setup(self)
	{
	}
}
class TCPSocketState()
{
	UnconnectedState = 0
	HostLookupState = 1
	ConnectingState = 2
	ConnectedState = 3
	BoundState = 4
	ListeningState = 5
	ClosingState = 6
}

class STcpSocket(Unit)
{
	def __init__(self)
	{
		self.readyRead = Signal()
        self.readyReadNewLine = Signal()
	}
	def connect(self, ip: str, port: int){}
	def close(self){}
	def write(self, data: str){}
	def readAll(self) -> str {}
	def flush(self){}
	def waitForReadyRead(self, msec : int){}
    def waitForConnected(self, msec : int){}
    def readLine(self) -> str {} 
    def clear(self) {}
	def getState(self) -> int {}
    def getBufferLength(self) -> int {}
	def moveToThread(self, thread) {}
    def setNewLine(self, newLine : str) {}
	def isValid(self) -> bool {}
}

class cadStra(STcpSocket)
{
    def __init__(self)
	{
		
	}
}

class STcpServer(Unit)
{
	def listen(self, port : int){}
	def close(self){}
	def write(self, data : str){}
	def readAll(self) -> str{}

}

class SSerialPort(Unit)
{
 	def __init__(self)
	{
        self.readyRead = Signal()
		self.readyReadNewLine = Signal()
    }

	def open(self, port: int, baudRate : int,  dataBits: int, parity : int ,stopBits:int, flowControl : int){}
	def close(self){}
	def readAll(self) -> str {}
	def write(self, data : str){}
}

class ctype_func()
{
	def call(self, *arg){}
	def restype(self, *arg){}
	def argtypes(self, *arg){}
}

class ctypes_cdll()
{
	def loadProc(self, procName : str)
	{}
	def registerCallbackFunc(self, *arg)
	{}
	def __init__(self, path : str) {

		self.path = path
	}
}

#class tuple()
#{
#	def __init__(self) {}
#	def get(self, idx: int){}
#	def count(self)->int{}
#}

class SFile()
{
	def open(self, filename: str, flag: str) {}
	def close(self) {}
	def read(self) {}
	def readline(self) {}
	def readlines(self) {}
	def write(self, text: str) {}
    def setPath(self, path : str) {}
    def readAll(self) {}
}

class SThread()
{

	def __init__(self)
	{
	}

	def start(self){}
	def setObjectName(self, strName: str){}
}

class HeartCore(Unit)
{

	def __init__(self)
	{
		self.signalLoop = Signal()
	}

	def start(self){}
	def subscribe(self, signal: Signal){}
	def loop(self){}
	def preStart(self){}
	def postStart(self){}
	def onTimer(self){}
	def quit(self){}
}

class Heart(HeartCore)
{
	def __init__(self)
	{
		self.parent: Unit = None
		self.children = list()
	}

	def loop(self)
	{
	}
}

class Message()
{
	def __init__(self)
	{
	}
}

class UIMessage(Message)
{
	def __init__(self)
	{
	}
}

class UIReqMessage(UIMessage)
{
	def __init__(self)
	{
	}
}

class UIRspMessage(UIMessage)
{
	def __init__(self, reqMsg: UIReqMessage)
	{
		self.reqMsg = reqMsg
	}
}

class MsgTimeout(Message)
{
	def __init__(self, msTimeout: int)
	{
		self.msTimeout = msTimeout
	}
}

class ActorRef(Unit)
{

	def __init__(self, getName : Callable[[], str], tell : Callable[[Message, ActorRef], None])
	{
		self.getName = getName
		self.tell = tell;
	}
}

class MessageInfo()
{
	def __init__(self, msg: Message, sender: ActorRef)
	{
		self.msg : Message = msg;
		self.sender : ActorRef = sender;
	}
}

class Mailbox(Unit)
{

	def __init__(self)
	{
		self._queue = deque()
		self.signalArrived = Signal()
		self._queue.signalAppended.connect(self.signalArrived)

		self.mutex = SMutex()
	}
	def enqueue(self, msg: Message, sender: ActorRef)
	{
		self.mutex.lock()

		msginfo = MessageInfo(msg, sender)
		self._queue.append(msginfo)

		self.mutex.unlock()
	}
	def dequeue(self) -> MessageInfo
	{
		return self._queue.popleft()
	}
	def count(self) -> int
	{
		return self._queue.count()
	}
	def at(self, idx: int) -> MessageInfo
	{
		return self._queue.at(idx)
	}
	def removeAt(self, idx: int)
	{
		self._queue.removeAt(idx)
	}
	def clear(self)
	{
		self._queue.clear()
	}
	def clearMessageBox(self)
   {
      for i in range(self.count())
      {
			value = self.at(i).msg
			if(isinstance(value, MessageBox.Ok))
			{
				self.removeAt(i)
			}
			elif(isinstance(value,MessageBox.Cancel))
			{	
				self.removeAt(i)
			}
        }
   }
}

class Actor(Heart)
{

	def setParent(self, parent: ActorKing)
	{
		self.parentActor = parent
		self.parentActor.children.append(self)
	}
	def __init__(self, name: str)
	{
		Heart.__init__(self)
		self.name = name
		self._mailbox = Mailbox()
		self.subscribe(self._mailbox.signalArrived)
		self.signalLoop.connect(self.fLoop)

		self.actorRef : ActorRef = ActorRef(self.getName, self.tell)
	}

	def tell(self, msg: Message, sender: ActorRef)
	{
		self._mailbox.enqueue(msg, sender)
	}

	def fLoop(self)
	{
#		print("got! fLoop()")
		while(self._mailbox.count() > 0)
		{
			msginfo : MessageInfo = self._mailbox.dequeue();
			self._msgHandler(msginfo.msg, msginfo.sender)
		}
	}

	def _msgHandler(self, msg: Message, sender: ActorRef)   #Actor
	{
	}

	def getSelf(self)
	{
		return self.actorRef
	}

	def getName(self) -> str
	{
		return self.name
	}

	def getUnit(self, upath: str)
	{
        strList = upath.split("/")
        i = 0
        count = strList.count()

        ret = None

        curUnit = self

        while(i < count)
        {
            strItem = strList.get(i)
            length = len(strItem)
            i = i + 1

            if(length == 0)
            {
                continue
            }

            if(hasattr(curUnit, upath))
            {
                curUnit = getattr(curUnit, upath)
                ret = curUnit
                continue
            }
            ret = None
            break
        }
        return ret
	}

	def getUnitList(self, upath: str)
	{
		listRtn = list()

		strList = upath.split("/")
		i = 0
		count = strList.count()

		isLowRank = false

		if(count != 0)
		{
			strItem = strList.get(count - 1)
			length = len(strItem)

			if(length == 0)
			{
				isLowRank = true
			}
		}

		ret = self
		curUnit = self

		while(i < count)
		{
			strItem = strList.get(i)
			length = len(strItem)
			i = i + 1

			if(length == 0)
			{
				continue
			}

			if(hasattr(curUnit, strItem))
			{
				curUnit = getattr(curUnit, strItem)
				ret = curUnit
				continue
			}
			ret = None
			break
		}

		if(ret != None)
		{
			if(isLowRank)
			{
				attrs = vars(ret)
				values = attrs.values()
				keys = attrs.keys()
				size = values.count()

				i = 0

				while(i < size)
				{
					attr = values.get(i)

					if(isinstance(attr, Variable))
					{
						upathUnit = upath + keys.get(i)

						tpUnit = (upathUnit, attr)
						listRtn.append(tpUnit)
					}

					i = i + 1
				}
			}
			else
			{
				tpUnit = (upath, ret)
				listRtn.append(tpUnit)
			}
		}

        return listRtn
	}

}


class State()
{
	def __init__(self, name: str)
	{
		self.oo = name
	}

	def getName(self) -> str
	{
		return self.oo
	}
}

class Action()
{
	def __init__(self, fnAction: function, liState: list)
	{
		self._fnAction = fnAction
		self.liState = liState
	}
}

class Transition()
{
	def __init__(self, typeMsg, stBefore, fnAction: function)
	{
		self._typeMsg 	= typeMsg
		self._stBefore 	= stBefore
		self._fnAction 	= fnAction
		self._action = None
	}

	def getTypeMsg(self)
	{
		return self._typeMsg
	}

	def getStateBefore(self)
	{
		return self._stBefore
	}

	def getAction(self)
	{
		return self._action
	}
}

class FSM(Unit)
{

	def __init__(self, name: str)
	{
		self.name = name
		self._dictState = dict()
		self._liTransition = list()
		self._dictTransition = dict()
		self.signalPreStateChanged = Signal()
		self.signalStateChanged = Signal()
#		self.signalLastSenderChanged = Signal()
		self.signalErrorStateChanged = Signal()
		self.__st: State = None
        self.initStateKernal : State = None
		self.dictActionRecipe = dict()
	}

	def addState(self, st, timeout: int)
	{
		self._dictState.set(st, timeout)
	}

	def addTransition(self, tr: Transition)
	{
		self._liTransition.append(tr)

	    if(!self._dictTransition.contains(tr._typeMsg))
    	{
	      self._dictTransition.set(tr._typeMsg, dict())
    	}

		_dictStateAction : dict = self._dictTransition.get(tr._typeMsg)
		_dictStateAction.set(tr._stBefore, tr._fnAction)
	}
	
	def addActionRecipe(self, action : function, executer : RecipeExecuter)
	{
		self.dictActionRecipe.set(action, executer)
	}

	def initState(self, st: State)
	{
        self.initStateKernal = st
		#self.setState(st)
	}

	def setState(self, st: State)
	{
		self.__st = st

        self.signalStateChanged.emit()
	}
	def doAction(self, msg : Message , action : function, sender : ActorRef)
	{	
		#                self.signalLastSenderChanged.emit(sender)

				try
				{
					if(self.dictActionRecipe.contains(action))
					{
						executer = self.dictActionRecipe.get(action)
						executer.work()
					}				
					
					self.__st : State = action(self.__st, msg, sender)
				}
				except Exception
				{
					self.__st : State = FSMActor.Error()
				}

				if(isinstance(self.__st, FSMActor.Error))
				{
					self.signalErrorStateChanged.emit()
				}

#				self._tm = time()
#				self._tm.sleep(1)

				self.setState(self.__st)
	}
	def _msgHandler(self, msg: Message, sender: ActorRef)   #FSM
	{
		if(self._dictTransition.contains(type(msg)))
		{
			dict2 : dict = self._dictTransition.get(type(msg))
			if(dict2.contains(type(self.__st)))
			{
				self.signalPreStateChanged.emit()

				actionFunction = dict2.get(type(self.__st))

				self.doAction(msg, actionFunction, sender)

				return true
			}
			elif(dict2.contains(None))
			{	
				self.signalPreStateChanged.emit()

				actionFunction = dict2.get(None)
				
				self.doAction(msg ,actionFunction, sender)
                
                return true
			}
		}
		else {
			return None
		}

		return false
	}

	def setParent(self, actor: ActorRef)
	{
		self.parentActor : ActorRef = actor;
	}

	def isAlive(self, msg: Message)
	{
		if(self._dictTransition.contains(type(msg)))
		{
			dict2 : dict = self._dictTransition.get(type(msg))

			if(dict2.contains(type(self.__st)))
			{
				return true
			}
		}

		return false
	}
}


class FSMActor(Actor)
{
	class Error(State)
	{
		def __init__(self)
		{
		}
	}

	class anystate(State)
	{
		def __init__(self)
		{
		}
	}	

    class MsgError(Message)
    {
        def __init__(self)
        {

        }
    }

	class MsgNotifyError(Message)
	{
		def __init__(self, actor: ActorRef)
		{
			self.actor = actor
		}
	}

	class MsgReset(Message)
	{
		def __init__(self)
		{
		}
	}
	class MsgResetAll(Message)
	{
		def __init__(self)
		{
		}
	}

	class MsgClearMsgBox(Message)
	{
		def __init__(self)
		{
		}
	}

	def __init__(self, name: str)
	{
		Actor.__init__(self, name)
		self._fsm = FSM(name)
		self._tm = time()
		self._fsm.setParent(self.getSelf())
		self._fsm.signalPreStateChanged.connect(self.preStateChanged)
		self._fsm.signalStateChanged.connect(self.stateChanged)
#        self._fsm.signalLastSenderChanged.connect(self.changedSender)
		self._fsm.signalErrorStateChanged.connect(self.changeErrorState)
		self.bufferMailbox = Mailbox()

#        self.lastSender = None
        self.setChildActorRef = set() # useless? yhkim
		
		self.timerTimeout = None
	}
	def clearMailBox(self)
	{
		self._mailbox.clear()
		self.bufferMailbox.clear()
	}
	
	def config(self)
	{
        attrs = vars(self)
        values = attrs.values()

        size = values.count()

        i = 0

        while(i < size)
        {
            child : Actor = values.get(i)
            if(isinstance(child, Actor))
            {
                self.setChildActorRef.add(child.getSelf())
            }

            i = i + 1
        }
	}

#    def changedSender(self, sender: Actor)
#    {
#        if(self.getName() != sender.getName())
#        {
#            if(!self.setChildActorRef.contains(sender))
#            {
#                self.lastSender = sender
#            }
#
#        }
#    }
	def changeErrorState(self)
	{
		self.parentActor.tell(FSMActor.MsgError(), self.getSelf())
	}
	def addState(self, st, timeout: int)
	{
		self._fsm.addState(st, timeout)
	}

	def addAction(self, ac: Action)
	{
		action = ac
	}

	def addTransition(self, tr: Transition)
	{
		self._fsm.addTransition(tr)
	}
	
	def addActionRecipe(self, action : function, listVar : list)
	{
		executer = RecipeExecuter(self, listVar)
			
		self._fsm.addActionRecipe(action, executer)
	}

	def initState(self, st: State)
	{
		self._fsm.initState(st)
	}

	def _msgHandler(self, msg: Message, sender: ActorRef)   #FSMActor
	{
		rtn = self._fsm._msgHandler(msg, sender)

		if(rtn == false)
		{
			if(type(msg) != BasicMessages.MsgBypass)
			{
				self.bufferMailbox.enqueue(msg, sender)
			}
		}

		if(isinstance(msg, FSMActor.MsgNotifyError))
		{
			pass
		}

		if(isinstance(msg, FSMActor.MsgResetAll))
		{
			self.parentActor.resetAll(self)
		}
		return rtn
	}
    def postStart(self)
	{
		#if(self.timerTimeout == None)
		#{
		#	self.timerTimeout.setSingleShot(true)
		#	self.timerTimeout.connect(self.generateTimeoutMessage)
		#}
        self._fsm.setState(self._fsm.initStateKernal)
	}
	def preStateChanged(self)
	{
		if(self.timerTimeout != None)
		{
			self.timerTimeout.stop()
		}
	}

	def stateChanged(self)  #FSMActor
	{
		timeout = 0

		if(self._fsm._dictState.contains(type(self._fsm.__st)))
		{
			timeout = self._fsm._dictState.get(type(self._fsm.__st))
		}

		if(timeout != 0)
		{
			if(self.timerTimeout == None)
			{
				self.timerTimeout = STimer()
				self.timerTimeout.setSingleShot(true)
				self.timerTimeout.connect(self.generateTimeoutMessage)
			}
			
			self.timerTimeout.start(timeout)
		}

		index = 0
		result = false

		while(self.bufferMailbox.count() > index)
		{
			if(result == false)
			{
				msgInfo = self.bufferMailbox.at(index)

				if(self._fsm.isAlive(msgInfo.msg))
				{
					result = true
					aliveMsgInfo = msgInfo
					self.bufferMailbox.removeAt(index)
				}
			}

			index = index + 1
		}

		if(result == false)
		{
            #self.tell(BasicMessages.MsgBypass(),self.getSelf())
			#self._msgHandler(BasicMessages.MsgBypass(), self.getSelf()) 
            if(self._fsm.isAlive(BasicMessages.MsgBypass()))
            {
                self._mailbox.enqueue(BasicMessages.MsgBypass(), self.getSelf())
            }
		}
		else
		{
			self._msgHandler(aliveMsgInfo.msg, aliveMsgInfo.sender)
		}
	}

	def generateTimeoutMessage(self)
	{
		#print("Timeout!!!!!!!!!!!!!!!!!!!")
		self.tell(MsgTimeout(0), self.getSelf())
	}
}

class ActorKing(FSMActor)
{

    def __init__(self, name: str)
    {
        FSMActor.__init__(self, name)
    }

	def _msgHandler(self, msg: Message, sender: ActorRef)
	{
		if(isinstance(msg, FSMActor.MsgError))
		{
			self.notifyError(sender)
		}
	}

	def notifyError(self, actor: ActorRef)
	{
        size = self.children.count()

        i = 0

        while(i < size)
        {

            child : Actor = self.children.get(i)
            if(isinstance(child, Actor))
            {
				if(child.name == actor.getName())
				{
					i = i + 1
					continue
				}
                child.tell(FSMActor.MsgNotifyError(actor), self.getSelf())
            }

            i = i + 1
        }
	}

	def resetAll(self, actor : Actor)
	{
		let size = self.children.count()
        i = 0

        while(i < size)
        {
            child : Actor = self.children.get(i)

            if(isinstance(child, FSMActor))
            {
                child.tell(FSMActor.MsgReset(), actor.getSelf())
            }

            i = i + 1
        }
		self.clearMailBox()
	}
}

class DataExchangeable()
{
	class AbstractExMsg()
	{
		def __init__(self)
		{
			self.upath : str = ""
			self.x : int = 0
			self.y : int = 0
		}
	}

	class ExMsgMeta(AbstractExMsg)
	{
		def __init__(self, typeContainer: type)
		{
			DataExchangeable.AbstractExMsg.__init__(self)
			self.typeContainer = typeContainer
			self.length = 0
			self.li = list()
		}
	}



	class ExMsgData(AbstractExMsg)
	{
		def __init__(self, data)
		{
			DataExchangeable.AbstractExMsg.__init__(self)
			self.data = data
			self.idx : int = 0
		}
	}

	class ExMsgDataIndex(ExMsgData)
	{
		def __init__(self, idx: tuple, data)
		{
			DataExchangeable.ExMsgData.__init__(self, data)
			self.idx : tuple = idx
		}
	}

	def __init__(self, data, typeContainer: type)
	{
        self.data = data
        self.typeContainer = typeContainer
        self.signalPublish = Signal()
	}

	def _contribute(self, value: DataExchangeable.AbstractExMsg)
    {
        if(isinstance(value, DataExchangeable.ExMsgData))
        {
			value: DataExchangeable.ExMsgData
			self._setDataMsg(value)
        }

        if(isinstance(value, DataExchangeable.ExMsgMeta))
        {
			value: DataExchangeable.ExMsgMeta
			self._setMetaMsg(value)
        }
    }

    def _publish(self, data: AbstractExMsg)
    {
        self.signalPublish.emit(data, self)
    }

	def _publishData(self, tpIdx: tuple)
	{

	}

    def _setDataMsg(self, data: ExMsgData)
    {

    }

    def _getDataMsg(self) -> ExMsgData
    {
        return DataExchangeable.ExMsgData(self.data)
    }

	def _getMetaMsg(self) -> ExMsgMeta
    {
        meta = DataExchangeable.ExMsgMeta(self.typeContainer)

		 meta.length = 1

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, VariableMetaAbstract))
            {
                meta.li.append(attr)
            }

            # if(isinstance(attr, Variable))
            # {
                # attrName = keys.get(i)
                # meta.liPath.append(attrName)
            # }

            i = i + 1
        }

        return meta
    }

	def _setMetaMsg(self, data: ExMsgMeta)  #Variable
    {
        meta = self._getMetaMsg()

        self._publish(meta)
    }

	def _findChild(self, typeChild: type)
    {
        attrs = vars(self)
        values = attrs.values()

        ret = None

        i = 0

        size = values.count()

        while(i < size)
        {
            child = values.get(i)

            if(isinstance(child, typeChild))
            {
                ret = child
                break
            }

            i = i + 1
        }

        return ret
    }

	def set(self, data)
	{
	}

	def get(self)
	{
	}
}

class RspVarList(DataExchangeable.AbstractExMsg)
{
    def __init__(self)
    {
        DataExchangeable.AbstractExMsg.__init__(self)

        self.liPath = list()
        self.liData = list()
    }
}

class VariableMetaAbstract(Unit)
{

    def __init__(self)
    {
        Unit.__init__(self)
    }
}

class VariableDesc(VariableMetaAbstract)
{

    def __init__(self, title: str, unit: str)
    {
        VariableMetaAbstract.__init__(self)

        self.title = title
        self.unit = unit
    }
}

class VariableDescList(VariableMetaAbstract)
{
    def __init__(self, titleList: list, unitList : list)
    {
        VariableMetaAbstract.__init__(self)

        self.titleList = titleList
        self.unitList = unitList
    }
}

class VariableRange(VariableMetaAbstract)
{

    def __init__(self, min, max, default)
    {
        VariableMetaAbstract.__init__(self)

        self.min = min
        self.max = max
        self.default = default
    }
}

class VariableRangeList(VariableMetaAbstract)
{
    def __init__(self, minList : list, maxList : list, defaultList : list)
    {
        VariableMetaAbstract.__init__(self)

        self.minList = minList
        self.maxList = maxList
        self.defaultList = defaultList
    }
}

class UIListenActor(Actor)
{

	class MsgListenedNotification(Message)
	{
		def __init__(self)
		{
		}
	}

	class MsgStartListening(Message)
	{
		def __init__(self)
		{
		}
	}
	def __init__(self, name: str)
	{
		Actor.__init__(self, name)
		self.uiActor : ActorRef = None
		self.timer = time()
	}

	def _msgHandler(self, msg: Message, sender: ActorRef)
    {
		if(isinstance(msg, UIListenActor.MsgStartListening))
		{
			self.listenLoop()
		}
	}

	def listenLoop(self)
	{
		while(true)
		{
			msleep(1000)

			let bListen = listenToNotify()

			if(!bListen)
			{
				i = 0
			}

			if(bListen)
			{
				self.uiActor.tell(UIListenActor.MsgListenedNotification(), self.getSelf())
			}
		}
	}
}

class UIActor(Actor)
{

	class MsgCallMessageBox(Message)
	{
		def __init__(self, uuid: str, type : int, data)
		{
			self.data = data
			self.type = type
			self.uuid = uuid
		}
	}
    class MsgCallBusyBox(Message)
    {
        def __init__(self, uuid:str, type : bool)
		{
            self.uuid = uuid
            self.type = type
		}
    }
	class MsgCloseMessageBox(Message)
	{
		def __init__(self, uuid: str)
		{
			self.uuid = uuid
		}
	}
	class MsgCallNumpadBox(Message)
	{
		def __init__(self, min : int, max :int, default : int)
		{
			self.min = min
			self.max = max
			self.default = default
		}
	}
	class MsgBehaviour(Message)
	{
		def __init__(self, behaviour : AtomBehaviour)
		{
			self.behaviour = behaviour
		}
	}
	
	class MsgReqAxisList(UIReqMessage)
	{
		def __init__(self)
		{
		}
	}
	class MsgReqAxisDataList(UIReqMessage)
	{
		def __init__(self)
		{
		}
	}
	class MsgReqData(UIReqMessage)
	{
		def __init__(self, upath : str)
		{
			self.upath = upath
		}
	}


	class MsgRspAxisList(UIRspMessage)
	{
		def __init__(self, reqMsg, sender: str, data)
		{
			self.reqMsg = reqMsg
			self.sender = sender
			self.data = data
		}
	}

    class MsgRspAxisDataList(UIRspMessage)
	{
		def __init__(self, reqMsg, sender: str, data)
		{
			self.reqMsg = reqMsg
			self.sender = sender
			self.data = data
		}
	}
	class MsgRspData(UIRspMessage)
	{
		def __init__(self, reqMsg, sender: str, data)
		{
			self.reqMsg = reqMsg
			self.sender = sender
			self.data = data
		}
	}

	class MsgReqIOList(UIReqMessage)
	{
		def __init__(self)
		{
		}
	}

	class MsgRspIOList(UIRspMessage)
	{
		def __init__(self, reqMsg, sender: str, data)
		{
			self.reqMsg = reqMsg
			self.sender = sender
			self.data = data
		}
	}

    class MsgSubscribe(UIMessage)
    {
        def __init__(self, subscriber: str, upath: str)
        {
            self.subscriber = subscriber
            self.upath = upath
        }
    }

    class MsgPublish(UIMessage)
    {
		def __init__(self, sender: str, upath: str, data)
		{
			self.sender = sender
			self.upath = upath
			self.data = data
		}
    }

    class MsgContribute(UIMessage)
    {
		def __init__(self, name: str, upath: str, data: AbstractExMsg)
		{
			self.name = name
			self.upath = upath
			self.data = data
		}
    }

	def __init__(self, name: str, listActors: list)
	{
		Actor.__init__(self, name)

        self.listActors = listActors

		self._dict = dict()
        self.dict_action = dict()
		self.dict_ActionSubscribe = dict()
		self.dict_Request = dict()
		self.dict_MessageBox = dict()
		self.dict_ActorRef = dict()
        self.dict_BusySender = dict()
		self.dict_Behaviour = dict()

		self.listeningActor = UIListenActor("Listener")
		self.listeningActor.uiActor = self.getSelf()
		self.listeningActor.start()
		self.listeningActor.tell(UIListenActor.MsgStartListening(), self.getSelf())

		self.signalOpenLogView = Signal()
		
		self.listIOControls = list()
	}

    def _msgHandler(self, msg: Message, sender: ActorRef)
    {
        name = sender.getName()

		if(isinstance(msg, UIActor.MsgBehaviour))
		{
			if(self.dict_Behaviour.contains(msg.behaviour))
			{
				signal : Signal = self.dict_Behaviour.get(msg.behaviour)
				self.dict_Behaviour.pop(msg.behaviour)
				signal.emit()
			}
		}

		if(isinstance(msg, UIRspMessage))
		{
			#msg : UIRspMessage
			dict2 : dict = self.dict_Request.get(name)
            if(dict2.contains(type(msg.reqMsg)))
            {
               signal : Signal = dict2.get(type(msg.reqMsg))
			   dict2.pop(type(msg.reqMsg))
               signal.emit(msg)
            }
		}

        if(self._dict.contains(name))
        {
            dict2 : dict = self._dict.get(name)
            if(dict2.contains(type(msg)))
            {
               signal : Signal = dict2.get(type(msg))
               signal.emit(msg)
            }
        }

        if(self._dict.contains(None))
		{
			dict2 : dict = self._dict.get(None)
            if(dict2.contains(type(msg)))
            {
               signal : Signal = dict2.get(type(msg))
               signal.emit(msg)
            }
		}

        if(isinstance(msg, UIActor.MsgPublish))
        {
            if(self.dict_action.contains(msg.sender))
            {
                dictPath : dict = self.dict_action.get(msg.sender)

                if(dictPath.contains(msg.upath))
                {
                    liSignal : list = dictPath.get(msg.upath)
					listCount : int = liSignal.count()

					idx = 0

					while(idx < listCount)
					{
						signal = liSignal.get(idx)
						signal.emit(msg)
						idx = idx + 1
					}
                }
            }
        }
		
        if(isinstance(msg, UIActor.MsgCallBusyBox))
        {
          # msg:UIActor.MsgCallBusyBox
            if(msg.type == true)    # popup busyBox
            {
                if(self.dict_BusySender.contains(sender) == false)
                {
                    popupMessageBox = RichMessageBox()
                    popupMessageBox.setStandardButtons(RichMessageBox.StandardButton.NoButton)
                    popupMessageBox.setText("busy...")
                    self.dict_MessageBox.set(msg.uuid, popupMessageBox)
                    self.dict_BusySender.set(sender, msg.uuid)
                    popupMessageBox.show()
                }
                else
                {
                    busyBox = self.getMessageBox(sender)
                    busyBox.show()
                }

            }
            elif(msg.type == false) # hide busyBox
            {
                busyBox = self.getMessageBox(sender)
                busyBox.hide()
            }
        }
        elif(isinstance(msg, UIActor.MsgCallMessageBox))
		{
            popupMessageBox = RichMessageBox()
            popupMessageBox.setStandardButtons(msg.type)
            popupMessageBox.setUUid(msg.uuid)

			if(self.dict_MessageBox.get(msg.uuid) != None)
			{
				return None
			}

			if(isinstance(msg.data, str))
			{
				popupMessageBox.setText(msg.data)
			}
			if(isinstance(msg.data, MutableStr))
			{
				popupMessageBox.setMutableStr(msg.data)
			}
            
            self.dict_MessageBox.set(msg.uuid, popupMessageBox)
            self.dict_ActorRef.set(popupMessageBox, sender)
            popupMessageBox.buttonClicked.connect(popupMessageBox.checkButton)
            popupMessageBox.closeEvent.connect(popupMessageBox.slotClose)
            popupMessageBox.sigOKCancel.connectWithSender(popupMessageBox, self.slotMessageBoxPush)    
			popupMessageBox.setWindowTitle("Message")
            popupMessageBox.show()
		}
        elif(isinstance(msg, UIActor.MsgCallNumpadBox))
        {
            localNumpad = SNumpad(None, msg.min, msg.max, msg.default)
            localNumpad.onOkWithSender.connectWithSender(localNumpad, self.slotNumpadPush)
            localNumpad.onCancelWithSender.connectWithSender(localNumpad, self.slotNumpadPush)

            self.dict_ActorRef.set(localNumpad, sender)

            busyBox = self.getMessageBox(sender)
            busyBox.hide()

            localNumpad.show()
        }
		elif(isinstance(msg, UIActor.MsgCloseMessageBox))
		{
			messageBox = self.dict_MessageBox.get(msg.uuid)
			messageBox.close()
		}

		if(isinstance(msg, UIListenActor.MsgListenedNotification))
		{
			self.signalOpenLogView.emit()
		}
    }

    def getMessageBox(self, sender : ActorRef)
    {
        messageBoxUUid = self.dict_BusySender.get(sender)
        messageBox = self.dict_MessageBox.get(messageBoxUUid)
        return messageBox
    }

    def slotMessageBoxPush(self, messageBox, msg:Message)
    {
        sender = self.dict_ActorRef.get(messageBox)
        sender.tell(msg, self.getSelf())
		self.dict_MessageBox.pop(messageBox.uuid)
    }

	def slotNumpadPush(self, messageBox, number : int)
	{
        sender = self.dict_ActorRef.get(messageBox)

        busyBox = self.getMessageBox(sender)
        busyBox.show()

        sender.tell(BasicMessages.MsgTakeIOIdx(number - 1), self.getSelf()) #cancel tell -1
	}

	def register(self, name: str, msg: Type, action: function)
	{
		listActors : list = self.getActors()
        size : int = listActors.count()
        ret : bool = false
        i = 0

        while(i < size)
        {
            attr = listActors.get(i)

            i = i + 1

            if(!isinstance(attr, Actor))
            {
                continue
            }
			if(!self._dict.contains(name))
			{

				self._dict.set(name, dict())
			}

			dict2 : dict = self._dict.get(name)

			if(!dict2.contains(msg))
			{
				dict2.set(msg, Signal())
			}

			signal : Signal = dict2.get(msg)
			signal.connect(action)
#			if(isinstance(attr, Actor))
#			{
#				attr.tell(msg, attr.getSelf())
#			}
			ret = true
			break
        }
		return ret
	}

    def register2(self, name: str, upath: str, action: function)
    {
        size = self.listActors.count()
        ret : bool = false
        i = 0

        while(i < size)
        {
            attr : Actor = self.listActors.get(i)
			
            i = i + 1

            if(!isinstance(attr, Actor))
            {
                continue
            }

            if(attr.getName() != name)
            {
                continue
            }

            if(!self.dict_action.contains(name))
            {
                self.dict_action.set(name, dict())
            }

            dictPath : dict = self.dict_action.get(name)

            if(!dictPath.contains(upath))
            {
                dictPath.set(upath, list())
            }

			liSignal : list = dictPath.get(upath)
            signal = Signal()
            signal.connect(action)
			liSignal.append(signal)

            if(isinstance(attr, Actor))
            {
                attr.tell(UIActor.MsgSubscribe(name, upath), attr.getSelf())
            }
			ret = true
            break
        }
		return ret
    }

	def getActor(self, name: str) -> Actor
    {
        size = self.listActors.count()

        i = 0

        actor = None

        while(i < size)
        {
            attr = self.listActors.get(i)

            i = i + 1

            if(!isinstance(attr, Actor))
            {
                continue
            }

            if(attr.getName() != name)
            {
                continue
            }

            actor : Actor = attr
            break

        }

        return actor
    }

	def request(self, name: str, msg: Message, action: function)
	{
		actor = self.getActor(name)

		if(actor != None)
		{
			if(!self.dict_Request.contains(name))
			{
				self.dict_Request.set(name, dict())
			}

			dict2 : dict = self.dict_Request.get(name)

			if(!dict2.contains(type(msg)))
			{
				dict2.set(type(msg), Signal())
			}

			signal : Signal = dict2.get(type(msg))
			signal.connect(action)

			actor.tell(msg, actor.getSelf())
		}
	}

	def getActors(self)
	{
        size = self.listActors.count()

        i = 0

		listActors = list()

        while(i < size)
        {
            attr = self.listActors.get(i)

            i = i + 1

            if(isinstance(attr, Actor))
            {
                listActors.append(attr)
            }
        }

        return listActors
	}

    def contribute(self, name: str, upath: str, data: AbstractExMsg)
    {
        actor = self.getActor(name)
        actor.tell(UIActor.MsgContribute(name, upath, data), actor.getSelf())
    }
	
	def executeBehaviour(self, behaviour : AtomBehaviour)
	{
		if(behaviour.actor != None)
		{
			if(!self.dict_Behaviour.contains(behaviour))
			{
				self.dict_Behaviour.set(behaviour, Signal())
				
				signal = self.dict_Behaviour.get(behaviour)
				
				if(behaviour.callbackFunc != None)
				{
					signal.connect(behaviour.callbackFunc)
				}
				
				behaviour.actor.tell(UIActor.MsgBehaviour(behaviour), behaviour.actor.getSelf())
			}
		}
	}
}

class Variable(Unit, DataExchangeable)
{

    def __init__(self, data, typeContainer: type)
    {
		if(typeContainer != None)
		{
			assert(isinstance(data, typeContainer))
		}
		DataExchangeable.__init__(self, data, typeContainer)

		self.desc: VariableDesc = None
		self.range: VariableRange = None
    }

	def __deserializing__(self)
    {
        self.signalPublish = Signal()
    }

	def __jobChanging__(self, newObj)
	{
		newObj.signalPublish = self.signalPublish
	}
}

class VariableSingle(Variable)
{

    def __init__(self, data)
    {
        Variable.__init__(self, data, None)
    }

    def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
	def __jobChanging__(self, newObj)
	{
		Variable.__jobChanging__(self, newObj)
	}
    def __jobChanged__(self)
    {
		self.signalPublish.emit(DataExchangeable.ExMsgData(self.data), self)
    }

    def get(self)
    {
        return self.data
    }

    def set(self, value)
    {
        self.data = value
        self.signalPublish.emit(DataExchangeable.ExMsgData(self.data), self)
    }
	def _setDataMsg(self, data: ExMsgData) #variableSingle
    {
        self.set(data.data)
	}
}
class VariableListData(DataExchangeable.ExMsgData)
{
	def __init__(self, index: int, data)
	{
		DataExchangeable.ExMsgData.__init__(self, data)
		self.idx : int = index
	}
}
class VariableList(Variable)
{
    def __init__(self, data: list)
    {
        Variable.__init__(self, data, list)
		self.data.signalContentChanged.connect(self._publishData)
    }
	def config(self)
	{
		self.data.signalContentChanged.connect(self._publishData)
	}
	def _publishData(self, tpIdx: tuple)
	{
		msg : DataExchangeable.ExMsgData = self._getDataMsg()

		msg.idx = tpIdx.get(0)

		self.signalPublish.emit(msg, self)
	}
    def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
	def __deserialized__(self)
    {
        self.data.signalContentChanged.connect(self._publishData)
    }
	def __jobChanging__(self, newObj)
	{
		Variable.__jobChanging__(self, newObj)
	}
    def __jobChanged__(self)
    {
       emitData = DataExchangeable.ExMsgData(self.data)
       emitData.idx : int = -1
       self.signalPublish.emit(emitData, self)
    }
    def getCopy(self)
    {
        copyList = list()
        for i in range(self.data.count())
        {
            copyList.append(self.data.get(i))
        }
        return copyList
    }
    def get(self, idx: int)
    {
        return self.data.get(idx)
    }

    def set(self, idx: int, value)
    {
        self.data.set(idx, value)
    }
	def _setDataMsg(self, data: ExMsgData) #variable List
    {
		if(isinstance(self, VariableCoord))
		{
			self: VariableCoord
			self.set(data)
		}
		else
		{
			self: VariableList
			self.set(data.idx, data.data)
		}
	}
	def _setMetaMsg(self, data: ExMsgMeta)  #Variable
    {
		currentVDL = None
		newVDL = None

		for i in range(data.li.count())
		{
			element = data.li.get(i)
			
			if(isinstance(element, VariableDescList))
			{
				newVDL = element
			}
		}
		
		if(newVDL != None)
		{
			attrs = vars(self)
			values = attrs.values()
			
			for i in range(values.count())
			{
				attr = values.get(i)
				
				if(isinstance(attr, VariableDescList))
				{
					currentVDL = attr
				}
			}
		}
		
		if(currentVDL != None)
		{
			if(currentVDL.titleList.count() == newVDL.titleList.count())
			{
				currentVDL.titleList.clear()
				
				for i in range(newVDL.titleList.count())
				{
					currentVDL.titleList.append(newVDL.titleList.get(i))
				}
			}
			
			if(currentVDL.unitList.count() == newVDL.unitList.count())
			{
				currentVDL.unitList.clear()
				
				for i in range(newVDL.unitList.count())
				{
					currentVDL.unitList.append(newVDL.unitList.get(i))
				}
			}
		}
		
        meta = self._getMetaMsg()

        self._publish(meta)
    }
	def _getMetaMsg(self) -> ExMsgMeta
    {
        meta = DataExchangeable.ExMsgMeta(self.typeContainer)

        meta.length = self.data.count()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, VariableMetaAbstract))
            {
                meta.li.append(attr)
            }

            # if(isinstance(attr, Variable))
            # {
                # attrName = keys.get(i)
                # meta.liPath.append(attrName)
            # }

            i = i + 1
        }

        return meta
    }
}

class VariableMatrix(Variable)
{

    def __init__(self, data: matrix)
    {
        Variable.__init__(self, data, matrix)
		  self.data.signalContentChanged.connect(self._publishData)
    }

    def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
    def __deserialized__(self)
    {
        self.data.signalContentChanged.connect(self._publishData)
    }
    def get(self, row : int, column : int)
    {
        return self.data.get(row, column)
    }

    def config(self)
    {
        self.data.signalContentChanged.connect(self._publishData)
    }

    def set(self, row : int, column: int, value)
    {
        self.data.set(row, column, value)
    }

	def _setDataMsg(self, data: ExMsgData)  #variableMatrix
    {
        self.set(data.y, data.x, data.data)
	}
	def _publishData(self, tpIdx: tuple)
	{
		msg : DataExchangeable.ExMsgData = self._getDataMsg()
       msg.y = tpIdx.get(0)
		msg.x = tpIdx.get(1)
		self.signalPublish.emit(msg, self)
	}
	def _getMetaMsg(self) -> ExMsgMeta
    {
        meta = DataExchangeable.ExMsgMeta(self.typeContainer)

        meta.length = self.data.column() * self.data.row()

		self.data : matrix = self.data #typehint
		meta.column = self.data.column()
		meta.row = self.data.row()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, VariableMetaAbstract))
            {
                meta.li.append(attr)
            }

            # if(isinstance(attr, Variable))
            # {
                # attrName = keys.get(i)
                # meta.liPath.append(attrName)
            # }

            i = i + 1
        }

        return meta
    }
}

class VariableCube(Variable)
{

    def __init__(self, data: cube)
    {
        Variable.__init__(self, data, cube)
        self.groupCountX = 1
        self.groupCountY = 1
    }
    def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
    def __deserialized__(self)
    {
        self.data.signalContentChanged.connect(self._publishData)
    }
    def get(self, row: int, column: int, depth: int)
    {
        return self.data.get(row, column, depth)
    }
    def config(self)
    {
    }

    def getRow(self)
    {
        return self.data.row()
    }
    def getColumn(self)
    {
        return self.data.column()
    }
    def getDepth(self)
    {
        return self.data.depth()
    }

    def set(self, row: int, column: int, depth: int, value)
    {
        self.data.set(row, column, depth, value)
    }
	def setNoSignal(self, row: int, column: int, depth: int, value)
    {
        self.data.setNoSignal(row, column, depth, value)
    }
	def _setDataMsg(self, data: ExMsgData) #variableCube
    {
		self.set(data.y, data.x, data.z, data.data)
	}

	def _publishData(self, tpIdx: tuple)
	{
		msg : DataExchangeable.ExMsgData = self._getDataMsg()
		msg.y : int = tpIdx.get(0)
		msg.x : int = tpIdx.get(1)
		msg.z : int = tpIdx.get(2)
		self.signalPublish.emit(msg, self)
	}
	class cubeMeta()
	{
		def __init__(self)
		{
			self.length = 0
			self.row = 0
			self.column = 0
			self.depth = 0
		}
	}
    def _getMetaMsg(self)
    {
        meta = self.cubeMeta()
        meta.length = self.data.row() * self.data.column() * self.data.depth()


		#self.data : cube = self.data #typehint
		meta.row = self.data.row()
		meta.column = self.data.column()
		meta.depth = self.data.depth()

       return meta
    }
}

class VariableCoord(VariableList)
{

	def __init__(self, listAxisName: list, listAxisData : list)
    {
		self._listAxisName = listAxisName;
		self._listAxis = list();

		axisCount = self._listAxisName.count()

		if(listAxisName.count() != listAxisData.count())
		{
			print("VariableCoord data isn\'t matched")
		}
        VariableList.__init__(self, listAxisData)
    }

    class ExCoordMsgMeta(DataExchangeable.ExMsgMeta)
    {
        def __init__(self, typeContainer : type, postFixList : list)
        {
            DataExchangeable.ExMsgMeta.__init__(self, typeContainer)
            self.postFixList = postFixList
        }
    }

	def getVector(self)
	{
		return vector(self.data)
	}
	def getSPoint(self) ->SPoint
	{
		return SPoint(self.data.get(0), self.data.get(1))
	}
    def getSPointF(self) -> SPointF
    {
        return SPointF(self.data.get(0), self.data.get(1))
    }
	def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
	def moveSync(self)
	{
		axisCount = self._listAxis.count()

		i = 0

		while(i < axisCount)
		{
			axis : Axis = self._listAxis.get(i)
			axis.move(self.get(i))
			i = i + 1
		}

		i = 0

		while(i < axisCount)
		{
			axis : Axis = self._listAxis.get(i)
			axis.wait()
			i = i + 1
		}
	}

	def synchronization(self)
	{
		axisCount = self._listAxis.count()

		i = 0

		while(i < axisCount)
		{
			axis : Axis = self._listAxis.get(i)
			pos = axis.getCmdPos()
			var = DataExchangeable.ExMsgData(pos);
			var.idx : int = i

			self.set(var)

			i = i + 1
		}
	}

	def set(self, data: DataExchangeable.ExMsgData)
    {
		VariableList.set(self, data.idx, data.data)
    }
	def getData(self, index : int)
	{
		return self.data.get(index)
	}
	def _getMetaMsg(self) -> ExCoordMsgMeta
    {
        meta = VariableCoord.ExCoordMsgMeta(self.typeContainer, self._listAxisName)

        meta.length = self.data.count()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, VariableMetaAbstract))
            {
                meta.li.append(attr)
            }

            i = i + 1
        }

        return meta
    }

}

class VariableMotionProfile(VariableList)
{

	def __init__(self, vel: float, accel: float, decel: float, jerk: float)
	{
		listParam = list()
		listParam.append(vel)
		listParam.append(accel)
		listParam.append(decel)
		listParam.append(jerk)

		VariableList.__init__(self, listParam)
	}
	def __deserializing__(self)
	{
		Variable.__deserializing__(self)
	}

	def setVel(self, vel: float)
	{
		data = DataExchangeable.ExMsgData(vel)

		VariableList.set(self, 0, data.data)
	}

	def setAccel(self, accel: float)
	{
		data = DataExchangeable.ExMsgData(accel)

		VariableList.set(self, 1, data.data)
	}

	def setDecel(self, decel: float)
	{
		data = DataExchangeable.ExMsgData(decel)

		VariableList.set(self, 2, data.data)
	}

	def setJerk(self, jerk: float)
	{
		data = DataExchangeable.ExMsgData(jerk)

		VariableList.set(self, 3, data.data)
	}

	def getVel(self)
	{
		return VariableList.get(self, 0)
	}

	def getAccel(self)
	{
		return VariableList.get(self, 1)
	}

	def getDecel(self)
	{
		return VariableList.get(self, 2)
	}

	def getJerk(self)
	{
		return VariableList.get(self, 3)
	}
}

class VariableMaterial(Variable)
{
	def __init__(self, layers: list)
	{
		Variable.__init__(self, None, None)

		self.liLayer = list()
		self.liDefault = list()

		listCount = layers.count()

		idx = 0
		while(idx < listCount)
		{
			tpLayer : tuple = layers.get(idx)
			name = tpLayer.get(0)
			value = tpLayer.get(1)

			self.liLayer.append(name)
			self.liDefault.append(value)

			idx = idx + 1
		}

		self.__cube : VariableCube = None
		self.__exist: VariableSingle = None
        self.__divider : VariableList = [1,1]
	}

	def __deserializing__(self)
    {
        Variable.__deserializing__(self)
    }
	def __jobChanging__(self, newObj)
	{
		Variable.__jobChanging__(self, newObj)
	}
	def config(self)
	{

		if(self.__cube != None)
		{
			#self.clear(self.__cube.data.row(), self.__cube.data.column())

			listCount = self.liLayer.count()

			idx = 0
			while(idx < listCount)
			{
				setattr(self, self.liLayer.get(idx), sliced_cube(self.__cube.data, idx))
				idx = idx + 1
			}

			self.__cube.signalPublish.connect(self.slotPublish)
		}

		if(self.__exist != None)
		{
			self.__exist.signalPublish.connect(self.slotPublish)
		}
	}
	def getLeftSideRowCol(self, find : int)
	{
		left = SRowCol(-1, -1)
		for i in range(self.column() / 2)
		{
			if(i % 2 == 0)
			{
				for j in range(self.row())
				{
					if(self.get(0, j, i) == find)
					{
						left.setColumn(i)
						left.setRow(j)
						return left
					}
				}
			}
			else
			{
				for j in range(self.row() - 1, -1, -1)
				{
					if(self.get(0, j, i) == find)
					{
						left.setColumn(i)
						left.setRow(j)
						return left
					}
				}
			}
		}
		return left
	}

	def getRightSideRowCol(self, find : int)
	{
		right = SRowCol(-1, -1)
		for i in range(self.column() / 2, self.column()) 
		{
			if(i % 2 == 0)
			{
				for j in range(self.row())
				{
					if(self.get(0, j, i) == find)
					{
						right.setColumn(i)
						right.setRow(j)
						return right
					}
				}
			}
			else
			{
				for j in range(self.row() - 1, -1, -1)
				{
					if(self.get(0, j, i) == find)
					{
						right.setColumn(i)
						right.setRow(j)
						return right
					}
				}
			}
		}
		return right
	}
	def getRowCol(self, find : int)
	{
		point = SRowCol(-1, -1)
		for i in range(self.column())
		{
			if(i % 2 == 0)
			{
				for j in range(self.row())
				{
					if(self.get(0, j, i) == find)
					{
						point.setColumn(i)
						point.setRow(j)
						return point
					}
				}
			}
			else
			{
				for j in range(self.row() - 1, -1, -1)
				{
					if(self.get(0, j, i) == find)
					{
						point.setColumn(i)
						point.setRow(j)
						return point
					}
				}
			}
		}
		return point
	}
	def getCount(self, value : int)
    {
        remainCnt = 0
        for row in range(self.row())
        {
            for col in range(self.column())
            {
                if(self.get(0, row, col) == value)
                {
                    remainCnt += 1
                }
            }
        }
        return remainCnt
    }
    def createTray(self, row : int, column : int, groupRow : int, groupColumn : int)
    {
        self.setExist(true)
        self.clear(row, column, groupRow, groupColumn)
    }
    def removeTray(self)
    {
        self.setExist(false)
    }
    def optimalModify(self, beforeValue : int, afterValue : int)
    {
    	pos = self.getRowCol(beforeValue)
		self.set(0, pos.getRow(), pos.getColumn(), afterValue)
    }
    def clearLayer(self, layer : int, value : int)
    {
        row = self.__cube.getRow()
        column = self.__cube.getColumn()
        for cRow in range(row)
		{
			for cCol in range (column)
			{
                self.__cube.set(cRow, cCol, layer, value)
			}
		}
    }
	def clear(self, row: int, column : int, groupRow : int, groupColumn : int)
	{
#		dt = DateTime()
#		print("clear")
#		print(dt.currentTime_ms())
		
		self.signalPublish.lock()
		self.__cube.signalPublish.lock()
		self.__cube.data.signalContentChanged.lock()
		
        row = row * groupRow
        column = column * groupColumn
        
		depth = self.liLayer.count()
#		self.__cube.data.clear()
		self.__cube.data.setSize(row, column, depth)
		
		for r in range(row)
		{
			for c in range(column)
			{
				for d in range(depth)
				{
					val = self.liDefault.get(d)
					self.__cube.setNoSignal(r, c, d, val)
				}
			}
		}
		
		self.__cube.data.emitChanged()
		
		self.signalPublish.unlock()
		self.__cube.signalPublish.unlock()
		self.__cube.data.signalContentChanged.unlock()
		
#		print(dt.currentTime_ms())

		dataType : DataExchangeable.ExMsgMeta = self._getMetaMsg()
		dataType.liLayer = self.listLayer()
        self._publish(dataType)

		initData = self.__cube._getDataMsg()
		self._publish(initData)

		initData = self.__exist._getDataMsg()
		self._publish(initData)
		
#		print(dt.currentTime_ms())
	}
    
	def get(self, layer: int, row: int, col: int)
	{
		return self.__cube.get(row, col, layer)
	}

	def set(self, layer: int, row: int, col: int, value)
	{
		self.__cube.set(row, col, layer, value)
	}

	def getExist(self)
	{
		return self.__exist.get()
	}

	def setExist(self, exist: bool)
	{
		self.__exist.set(exist)
	}

	def getLayer(self, name: str)
	{
		layer = -1

		listCount = self.liLayer.count()

		idx = 0
		while(idx < listCount)
		{
			if(self.liLayer.get(idx) == name)
			{
				layer = idx

				break
			}

			idx = idx + 1
		}

		if(layer != -1)
		{
			return sliced_cube(self.__cube.data, layer)
		}
	}

	def getSize(self)
	{
		return (self.__cube.data.row(), self.__cube.data.column())
	}

	def row(self)
	{
		return self.__cube.data.row()
	}

	def column(self)
	{
		return self.__cube.data.column()
	}

	def listLayer(self)
	{
		return self.liLayer
	}

	def slotPublish(self, data: AbstractExMsg, sender)
    {
		self.signalPublish.emit(data, self)
    }

	def _setDataMsg(self, data: ExMsgData)
    {
		if(hasattr(data, "z"))
		{
			self.__cube.set(data.y, data.x, data.z, data.data)
		}
		else
		{
			self.__exist.set(data.data)
		}
	}

    def _getMetaMsg(self) -> ExMsgMeta
    {
        meta = DataExchangeable.ExMsgMeta(self.typeContainer)
        meta.li.append(self.__cube._getMetaMsg())

        dividerList = [1, 1]
        if(self.__divider == None)
        {
            meta.li.append(dividerList)
        }
        else
        {
            dividerList.set(0, self.__divider.get(0))
            dividerList.set(1, self.__divider.get(1))
            meta.li.append(dividerList)
        }
        return meta
    }
}

class VariableRecipe(VariableSingle)
{
    def __init__(self)
    {
        VariableSingle.__init__(self, "")
    }
}

class BasicMessages()
{
	class MsgBypass(Message)
	{
	}

	class MsgBegin(Message)
	{
	}
    class MsgAuto(Message)
    {
		def __init__(self, obj)
		{	
			self.obj = obj
		}
    }
	class MsgEnded(Message)
	{
	}

	class MsgGo(Message)
	{
	}

	class MsgCancel(Message)
	{
	}

	class MsgStop(Message)
	{
	}

	class MsgOk(Message)
	{
	}

	class MsgisIdle(Message)
	{
	}

	class MsgDryRun(Message)
	{
		def __init__(self, obj)
		{
			self.obj = obj
		}
	}

    class MsgTrayBypass(Message)
	{
		def __init__(self)
		{
		}
	}

	class MsgHoming(Message)
	{
		def __init__(self)
		{
		}
	}
	class MsgDown(Message)
	{
		def __init__(self)
		{
		}
	}

	class MsgConfirmForHoming(Message)
	{
		def __init__(self)
		{
		}
	}
    class MsgTakeIOIdx(Message)
	{
		def __init__(self, idx : int)
		{
            self.idx = idx
		}
	}
}

class MessageBox()
{
    class Ok(Message)
    {
    }
    class Cancel(Message)
    {
    }
}


class Tray()
{
	def __init__(self)
	{
		self.state = list()

		index = 0

		while(index < 5)
		{
			self.state.append(0)
			index = index + 1

		}

	}
}

class Param(Unit)
{
	def __init__(self)
	{
	}
}

class MetaParam(Unit)
{
	def __init__(self)
	{
	}
}

class MetaParamRange(MetaParam)
{
}

class MetaParamDesc(MetaParam)
{
	def __init__(self, desc: str)
	{
		self.desc = desc
	}
}

class MetaParamPrivileges(MetaParam)
{
	def __init__(self, lvlView: int, lvlEdit: int)
	{
		self.lvlView: int = lvlView
		self.lvlEdit: int = lvlEdit
	}
}


class ParamInt(Unit)
{
	def __init__(self)
	{
		self.value: int = None
	}

	def get(self)
	{
		return self.value
	}

	def set(self, value: int)
	{
		self.value = value
	}
}


class MetaParamInt(MetaParamRange)
{
	def __init__(self, min: int, max: int, default: int)
	{
		self.min: int 		= min
		self.max: int 		= max
		self.default: int 	= default
	}
}


class ParamCoord(Unit)
{
	def __init__(self)
	{
		self.value: vector 	= None
		self.axes : Axes  	= None
		self.dim  : int		= None
	}

	def config(self)
	{
		self.dim 	= len(self.axes)
#		self.value  = vector_([None]*self.dim)
	}

	def get(self)
	{
		return self.value
	}

	def set(self, value: vector_)
	{
#		if len(value) != self.dim {
#			throw Exception("the dimension of the vector_ is different")
#		}
		self.value = value
	}
}

class MetaParamCoord(MetaParamRange)
{
	def __init__(self, min: vector_, max: vector_, default: vector_)
	{
		self.min: vector	= min
		self.max: vector	= max
		self.default: vector 	= default
	}
}

class AbstractController(Unit)
{
	def __init__(self, name: str)
	{
		self.name = name
		self.switch = None
	}

	def initialize(self)
	{
	}

	def terminate(self)
	{
	}
}

class AbstractMotionController(AbstractController)
{
	def __init__(self, name: str)
	{
		AbstractController.__init__(self, name)
	}

	def initialize(self)
	{
	}

	def terminate(self)
	{
	}

	def initMotor(self, axis: int, nOption: int)
	{
	}

	def setName(self, axis: int, name: str)
	{
	}

	def isAlarm(self, axis: int) -> bool
	{
        return false
	}

	def enable(self, axis: int, enable: bool)
	{
	}

	def isEnabled(self, axis: int) -> bool
	{
	}

	def moveSync(self, axis: int, pos: float)
	{
	}

	def relMove(self, axis: int, pos: float)
	{
	}

	def velMove(self, axis: int, reverse: bool)
	{
	}

	def move(self, axis: int, pos: float)
	{
	}

	def relMoveSync(self, axis: int, pos: float)
	{
	}

	def isMoving(self, axis: int) -> bool
	{
	}

	def getCmdPos(self, axis: int) -> float
	{
	}

	def getActPos(self, axis: int) -> float
	{
	}

	def stop(self, axis: int)
	{
	}

	def abort(self, axis: int)
	{
	}

	def ampFault(self, axis: int) -> bool
	{

	}

	def release_cmd(self, axis: int)
	{

	}

	def setPosition(self, axis: int, pos: float)
	{
	}

	def setAccel(self, axis: int, value: float)
	{
	}

	def setDecel(self, axis: int, value: float)
	{
	}

	def setJerk(self, axis: int, value: float)
	{
	}

	def setVelocity(self, axis: int, value: float)
	{
	}

	def clear(self, axis: int)
	{
	}

	def getLimitNStatus(self, axis: int) -> bool
	{
	}

	def getLimitPStatus(self, axis: int) -> bool
	{
	}

	def getHomeStatus(self, axis: int) -> bool
	{
	}

	def ClearSuperviser(self, axis1: int, axis2: int, union_axis: int) -> int
	{
	}

	def wait(self, axis: int)
	{
		msleep(10)

		while(self.isMoving(axis))
		{
			msleep(10)
		}
	}
    def panic(self)
    {
    
    }
}

class Axis(DataExchangeable, Unit)
{
	class Sensor()
	{
		PositiveLimit = 0
		NegativeLimit = 1
		Home = 2
		PositiveHome = 3
		NegativeHome = 4
	}

	class AxisCommand(DataExchangeable.ExMsgData)
	{
		def __init__(self, data)
		{
			DataExchangeable.ExMsgData.__init__(self, data)
		}
	}

	class AxisCommandSetName(AxisCommand)
	{
		def __init__(self, name: str)
		{
			Axis.AxisCommand.__init__(self, name)
		}
	}

	class AxisCommandEnable(AxisCommand)
	{
		def __init__(self, enable: bool)
		{
			Axis.AxisCommand.__init__(self, enable)
		}
	}

	class AxisCommandMove(AxisCommand)
	{
		def __init__(self, pos: float)
		{
			Axis.AxisCommand.__init__(self, pos)
		}
	}

	class AxisCommandRelMove(AxisCommand)
	{
		def __init__(self, pos: float)
		{
			Axis.AxisCommand.__init__(self, pos)
		}
	}

	class AxisCommandStop(AxisCommand)
	{
		def __init__(self)
		{
		}
	}

	class AxisCommandSetPosition(AxisCommand)
	{
		def __init__(self, pos: float)
		{
			Axis.AxisCommand.__init__(self, pos)
		}
	}

	class AxisCommandSetAccel(AxisCommand)
	{
		def __init__(self, value: float)
		{
			Axis.AxisCommand.__init__(self, value)
		}
	}

	class AxisCommandSetDecel(AxisCommand)
	{
		def __init__(self, value: float)
		{
			Axis.AxisCommand.__init__(self, value)
		}
	}

	class AxisCommandSetJerk(AxisCommand)
	{
		def __init__(self, value: float)
		{
			Axis.AxisCommand.__init__(self, value)
		}
	}

	class AxisCommandSetVelocity(AxisCommand)
	{
		def __init__(self, value: float)
		{
			Axis.AxisCommand.__init__(self, value)
		}
	}

	class AxisCommandClear(AxisCommand)
	{
		def __init__(self)
		{
		}
	}

	class AxisData(Mutable)
	{
		def __init__(self, axis: Axis)
		{
			Mutable.__init__(self, axis)
			self.instance : Axis = self.instance #typehint
			self.posCmd = 0.0
			self.posAct = 0.0
			self.enableState = false
			self.movingState = false
			self.faultState = false

			self.home = false
			self.negativeLimit = false
			self.positiveLimit = false
		}

		def read(self)
		{
			self.mutex.lock()
			self.posCmd = self.instance.getCmdPos()
			self.posAct = self.instance.getActPos()
			self.enableState = self.instance.isEnabled()
			self.movingState = self.instance.isMoving()
			self.faultState = self.instance.isAlarm()

			self.home = self.instance.getHomeStatus()
			self.negativeLimit = self.instance.getLimitNStatus()
			self.positiveLimit = self.instance.getLimitPStatus()

			self.mutex.unlock()
		}

		def write(self)
		{
			self.mutex.lock()
			self.instance.enable(self.enableState)
			self.instance.setPosition(self.posCmd)
			self.mutex.unlock()
		}
	}

	def __init__(self, index: int, ratio: float, motion_type: int, reverse_limit_p: bool, reverse_limit_n: bool, reverse_home: bool)
	{
		DataExchangeable.__init__(self, None, None)

		self.ctrlMotion : AbstractMotionController = None
		self.index = index
		self.ratio = ratio
		self.motion_type = motion_type
		self.reverse_limit_p = reverse_limit_p
		self.reverse_limit_n = reverse_limit_n
		self.reverse_home = reverse_home
		self.pos_target = 0.0
		self.pos_depart = 0.0

		self.profile: VariableMotionProfile = None
	}

	def _setDataMsg(self, data: ExMsgData)
    {
		if(isinstance(data, Axis.AxisCommandSetName))
		{
			self.setName(data.data)
		}

		if(isinstance(data, Axis.AxisCommandEnable))
		{
			self.enable(data.data)
		}

        if(isinstance(data, Axis.AxisCommandMove))
        {
			self.move(data.data)
        }

		if(isinstance(data, Axis.AxisCommandRelMove))
        {
			self.relMove(data.data)
        }

		if(isinstance(data, Axis.AxisCommandStop))
        {
			self.stop()
        }

		if(isinstance(data, Axis.AxisCommandSetPosition))
        {
			self.setPosition(data.data)
        }

		if(isinstance(data, Axis.AxisCommandSetAccel))
        {
			self.setAccel(data.data)
        }

		if(isinstance(data, Axis.AxisCommandSetDecel))
        {
			self.setDecel(data.data)
        }

		if(isinstance(data, Axis.AxisCommandSetJerk))
        {
			self.setJerk(data.data)
        }

		if(isinstance(data, Axis.AxisCommandSetVelocity))
        {
			self.setVelocity(data.data)
        }

		if(isinstance(data, Axis.AxisCommandClear))
        {
			self.clear()
        }

		if(!isinstance(data, Axis.AxisCommand))
		{
			DataExchangeable._setDataMsg(self, data)
		}
    }

	def _getDataMsg(self)
    {
        return Axis.AxisData(self)
    }

	def getOnPC(self) -> int
	{
		if(self.ctrlMotion.switch.get() == "virtual")
		{
			return true
		}
		return false
	}

	def convUmToPls(self, um: float)
	{
		return um * (self.ratio / 1000)
	}
	
	def convMmToPls(self, mm: float)
	{
		return mm * self.ratio
	}
	
	def convPlsToUm(self, pls: float)
	{
		return pls / self.ratio
	}
	
	def convPlsToMm(self, pls: float)
	{
		return pls / (self.ratio / 1000)
	}
		
	def setName(self, name: str)
	{
		self.ctrlMotion.setName(self.index, name)
	}

	def isAlarm(self)
	{
		return self.ctrlMotion.isAlarm(self.index)
	}

	def enable(self, enable: bool)
	{
		self.ctrlMotion.enable(self.index, enable)
	}

	def isEnabled(self)
	{
		return self.ctrlMotion.isEnabled(self.index)
	}

	def moveSync(self, pos: float)
	{
		if(self.isAlarm())
		{
			raise Exception()
		}
		self.pos_target = (float(pos))
		self.pos_depart = self.getCmdPos()
		self.ctrlMotion.moveSync(self.index, (float(self.convMmToPls(pos))))
	}

	def relMove(self, pos: float)
	{
		self.pos_target = (float(pos))
		self.pos_depart = self.getCmdPos()
		self.ctrlMotion.relMove(self.index, self.convMmToPls(pos))
	}

	def velMove(self, reverse: bool)
	{
		if(self.ratio < 0)
		{
			reverse = !reverse
		}
		self.ctrlMotion.velMove(self.index, reverse)
	}

	def move(self, pos: float)
	{
		pos_ = self.convMmToPls(pos)
		self.pos_target = (float(pos))
		self.pos_depart = self.getCmdPos()
		self.ctrlMotion.move(self.index, self.convMmToPls(pos))
	}

	def relMoveSync(self, pos: float)
	{
		self.pos_target = self.getCmdPos() + (float(pos))
		self.pos_depart = self.getCmdPos()
		self.ctrlMotion.relMoveSync(self.index, self.convMmToPls(pos))
	}

	def ClearSuperviser(self, axis1:int, axis2:int)
	{
		return self.ctrlMotion.ClearSuperviser(axis1, axis2, self.index)
	}

	def isMoving(self)
	{
		return self.ctrlMotion.isMoving(self.index)
	}

	def wait(self)
	{
		self.ctrlMotion.wait(self.index)
		dblActCur = self.getActPos()
		dblPosTarget = abs(self.pos_target)
		dblDiff = dblActCur - dblPosTarget
		nCnt = 0
		if(200 < dblDiff)
		{
			if(nCnt < 2)
			{
				msleep(1000)
				nCnt +=1
			}
			else
			{
				raise Exception()
			}
		}
	}

	def getCmdPos(self)
	{
		if(self.ctrlMotion.switch.data == "virtual")
		{
			posCmd = self.pos_target
		}
		else
		{
			posCmd = self.ctrlMotion.getCmdPos(self.index)
		}
		posCmdum = posCmd
		if(posCmd != 0)
		{
			posCmdum = posCmd / self.ratio
		}
		return posCmdum
	}

	def getActPos(self)
	{
		posAct = self.ctrlMotion.getActPos(self.index)
		posActum = posAct
		if(posAct != 0)
		{
			posActum = posAct / self.ratio
		}
		return posActum
	}

	def refreshTarget(self)
	{
		self.pos_target = self.getActPos(self.index)
	}

	def setTarget(self, pos: float)
	{
		self.pos_target = pos
	}

	def waitNear(self, pos: float)
	{
		msleep(10)

		if(self.getOnPC())
		{
			return true
		}
		actPos = self.getActPos()
		while(true)
		{
			actPos = self.getActPos()
			absPos = abs(actPos - self.pos_target)
			if(self.ampFault())
			{
				raise Exception()
			}
			if(self.isAlarm())
			{
				raise Exception()
			}
			if(!self.isMoving())
			{
				if(pos >= absPos)
				{
					return true
				}
			}
			if(pos >= absPos)
			{
				return true
			}

			msleep(1)
		}
	}

	def waitFar(self, pos: float)
	{
		msleep(10)

		if(self.getOnPC())
		{
			return true
		}
		actPos = self.getActPos()
		while(true)
		{
			actPos = self.getActPos()
			absPosTG = abs(actPos - self.pos_target)
			absPosDT = abs(actPos - self.pos_depart)
			if(self.ampFault())
			{
				raise Exception()
			}
			if(self.isAlarm())
			{
				raise Exception()
			}
			if(!self.isMoving())
			{
				if(absPosTG > pos)
				{
					raise Exception()
				}
			}
			if(absPosDT > pos)
			{
				return true
			}

			msleep(1)
		}
	}

	def stop(self)
	{
		self.ctrlMotion.stop(self.index)
	}

	def abort(self)
	{
		self.ctrlMotion.abort(self.index)
	}

	def ampFault(self)
	{
		return self.ctrlMotion.ampFault(self.index)
	}

	def release_cmd(self)
	{
		self.ctrlMotion.release_cmd(self.index)
	}

	def Find_Z_Phase(self, mode: int, pos: float)
	{
		nRet = -1
		pls_rev = pos * self.ratio
		vel = self.profile.getVel() / 10
		acc = self.profile.getAccel() / 10
		jerk = self.profile.getJerk()
		if(mode / 10 == 0)
		{
			if (0 != self.ctrlMotion.find_z_phase1(mode, self.index, pls_rev, vel, acc, jerk))
			{
				nRet = 1
				return nRet
			}
			msleep(100)
			if (0 != self.ctrlMotion.find_z_phase3(mode, self.index, pls_rev, vel, acc, jerk))
			{
				nRet = 3
				return nRet
			}
			msleep(500)
			self.clear()
			msleep(100)
			self.wait()
			if (0 != self.ctrlMotion.find_z_phase4(mode, self.index, pls_rev, vel, acc, jerk))
			{
				nRet = 4
				return nRet
			}
			nRet = 0
		}
		else
		{
			if (0 != self.ctrlMotion.find_z_phase1(mode, self.index, pls_rev, vel, acc, jerk))
			{
				nRet = 1
				return false
			}
			nCnt = 0
			while(true)
			{
				if (0 == self.ctrlMotion.find_z_phase2(mode, self.index, pls_rev, vel, acc, jerk))
				{
					nRet = 0;
					break
				}
				if(!self.isMoving())
				{
					nRet = 10
				}
				elif(self.ampFault())
				{
					nRet = 20
				}
				elif(nCnt >= 60000)
				{
					nRet = 30
				}
				if(-1 != nRet)
				{
					break
				}
				nCnt += 1
				msleep(1)
			}
			self.stop()
			msleep(500)
			self.clear()
			msleep(100)
			if(0 != nRet)
			{
				return nRet
			}
			if (0 != self.ctrlMotion.find_z_phase4(mode, self.index, pls_rev, vel, acc, jerk))
			{
				nRet = 4
				return nRet
			}
		}
		self.wait()
		self.setPosition(0)

		return nRet
	}
	
	def moveSeq(self, axis: int, pos1: float, vel1: float, acc1: float, pos2: float, vel2: float, acc2: float)
	{
		conv_jerk = self.convMmToPls(self.profile.getJerk())
		self.ctrlMotion.moveSeq(axis, pos1, vel1, acc1, conv_jerk, pos2, vel2, acc2, conv_jerk)
	}

	def moveSeq_Touch(self, axis: int, pos1: float, vel1: float, acc1: float, pos2: float, vel2: float, acc2: float, axis_enc: int, encoder_targer: float)
	{
		conv_jerk = self.convMmToPls(self.profile.getJerk())
		self.ctrlMotion.moveSeq_Touch(axis, pos1, vel1, acc1, conv_jerk, pos2, vel2, acc2, conv_jerk, axis_enc, encoder_targer, false)
	}
	
	def AutoLevel_SpdMode(self, startPos: float, vel: float, acc: float, axis_enc: Axis, encoder_targer_um: float)
	{
		nRet = -1
		self.moveSync(startPos - 2)
		conv_vel = self.convMmToPls(-vel)
		conv_acc = self.convMmToPls(acc)
		conv_jerk = self.convMmToPls(self.profile.getJerk())
		conv_target = axis_enc.convUmToPls(encoder_targer_um)
		nRet = self.ctrlMotion.AutoLevel_SpdMode(self.index, conv_vel, conv_acc, conv_jerk, axis_enc.index, conv_target, false)
		self.wait()
		self.SequenceStop()
		cmdPos = self.getCmdPos()
		dblAutoLevel = float(cmdPos + self.convUmToPls(encoder_targer_um))
		self.moveSync(startPos)
		return dblAutoLevel
	}
	
	def SequenceStop(self)
	{	
		return self.ctrlMotion._SequenceStop(self.index)
	}

	def setPosition(self, pos: float)
	{
		self.pos_target = pos
		self.pos_depart = pos
		self.ctrlMotion.setPosition(self.index, pos * self.ratio)
	}

	def setAccel(self, value: float)
	{
		if(self.profile != None)
		{
			self.profile.setAccel(value)

			self.ctrlMotion.setAccel(self.index, value * abs(self.ratio))
		}
	}

	def setDecel(self, value: float)
	{
		if(self.profile != None)
		{
			self.profile.setDecel(value)

			self.ctrlMotion.setDecel(self.index, value * abs(self.ratio))
		}
	}

	def setJerk(self, value: float)
	{
		if(self.profile != None)
		{
			self.profile.setJerk(value)

			self.ctrlMotion.setJerk(self.index, value * abs(self.ratio))
		}
	}

	def setVelocity(self, value: float)
	{
		if(self.profile != None)
		{
			self.profile.setVel(value)

			self.ctrlMotion.setVelocity(self.index, value * abs(self.ratio))
		}
	}

	def setProfile(self, profile: VariableMotionProfile)
	{
		self.profile = profile

		accel = self.profile.getAccel()
		decel = self.profile.getDecel()
		jerk = self.profile.getJerk()
		vel = self.profile.getVel()

        if(self.ctrlMotion.switch.get() == "mei")
        {
            self.ctrlMotion.setAccel(self.index, accel * abs(self.ratio))
            self.ctrlMotion.setDecel(self.index, decel * abs(self.ratio))
            self.ctrlMotion.setJerk(self.index, jerk * abs(self.ratio))
            self.ctrlMotion.setVelocity(self.index, vel * abs(self.ratio))	
        }
        elif(self.ctrlMotion.switch.get() == "comizoa")
        {
            self.ctrlMotion.setSpeedPattern(self.index, COMIZOAController.speedMode.cmSMODE_S, vel * abs(self.ratio) ,  accel * abs(self.ratio) , decel * abs(self.ratio))
        }
    }

	def clear(self)
	{
		self.ctrlMotion.clear(self.index)
	}

	def getLimitNStatus(self)
	{
		return self.ctrlMotion.getLimitNStatus(self.index)
	}

	def getLimitPStatus(self)
	{
		return self.ctrlMotion.getLimitPStatus(self.index)
	}

	def getHomeStatus(self)
	{
		return self.ctrlMotion.getHomeStatus(self.index)
	}

	def initMotor(self, nOption: int)
	{
		return self.ctrlMotion.initMotor(self.index, nOption)
	}

	def panic(self)
	{
		return self.ctrlMotion.panic()
	}

	def init_axis(self)
	{
		self.enable(false)
		msleep(100)
		self.clear()
		msleep(100)
		self.setPosition(0.0)
		msleep(100)
		self.clear()
		msleep(100)
		if(self.motion_type != 1)
		{
			self.enable(true)
			msleep(100)
		}
	}

	def homing(self, dir: int, sensor: Sensor)
	{
		if(self.ctrlMotion.switch.get() == "virtual")
		{
			return None
		}
		funcSensorCheck = None

		if(sensor == Axis.Sensor.NegativeLimit)
		{
			funcSensorCheck = self.getLimitNStatus
		}

		if(sensor == Axis.Sensor.PositiveLimit)
		{
			funcSensorCheck = self.getLimitPStatus
		}

		if(sensor == Axis.Sensor.Home)
		{
			funcSensorCheck = self.getHomeStatus
		}

		if(funcSensorCheck == None)
		{
			return None
		}

		if(self.profile == None)
		{
			return None
		}

		reverse = false
		if(dir < 0)
		{
			reverse = true
		}

		orgVel = self.profile.getVel()

		if(!funcSensorCheck())
		{
			self.velMove(reverse)
		}

		msleep(10)

		while(true)
		{
			if(funcSensorCheck())
			{
				self.stop()
				break
			}

			if(!self.isMoving())
			{
				break
			}

			msleep(10)
		}

		while(self.isMoving())
		{
			msleep(10)
		}

		self.ctrlMotion.setVelocity(self.index, orgVel * abs(self.ratio) / 10)

		self.velMove(!reverse)
		msleep(10)

		while(true)
		{
			if(!funcSensorCheck())
			{
				self.stop()
				break
			}

			if(!self.isMoving())
			{
				break
			}

			msleep(10)
		}

		while(self.isMoving())
		{
			msleep(10)
		}

		msleep(2000)

		self.setVelocity(orgVel)
		self.setPosition(0.0)
		msleep(100)
		self.clear()
	}

    def _getProfileList(self)
    {
        profileList = RspVarList()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, VariableMotionProfile))
            {
                attrName = keys.get(i)
                profileList.liPath.append(attrName)
            }

            i = i + 1
        }

        return profileList
    }
}

class Axes(Unit)
{
	def updateAxis(self)
	{
		attrs = vars(self)
		sortedItem = attrs.sortedItems()

		i = 0

		while( i < sortedItem.count() )
		{
			axis = sortedItem.get(i).get(1)
			if(isinstance(axis, Axis))
			{
				self._listAxis.append(axis)
			}
			i = i + 1
		}
	}

	def config(self)
	{
		self.updateAxis()
	}

	def __init__(self)
	{
		self._listAxis = list()
	}

	def moveSync(self, position : list)
	{
		i = 0
		while(i < self._listAxis.count())
		{
			self._listAxis.get(i).move(position.get(i))
			i = i + 1
		}
		i = 0
		while(i < self._listAxis.count())
		{
			self._listAxis.get(i).wait()
			i = i + 1
		}
	}

	def move(self, position : list)
	{
		i = 0
		while(i < self._listAxis.count())
		{
			self._listAxis.get(i).move(position.get(i))
			i = i + 1
		}
	}
	def wait(self, position : list)
	{
		i = 0
		while(i < self._listAxis.count())
		{
			self._listAxis.get(i).wait()
			i = i + 1
		}
	}
}
class AbstractIOController(AbstractController)
{
	def __init__(self, name: str)
	{
		AbstractController.__init__(self, name)
	}

	def getDigital(self, idx: int) -> float
    {
	}

	def setDigital(self, idx: int, bVal: bool)
	{
	}

	def getDigitalInternal(self, idx: int) -> float
	{
	}

	def getAnalog(self, index: int) -> bool
	{
	}

	def setAnalog(self, index: int, value: float)
	{
	}

	def getAnalogInternal(self, index: int) -> bool
	{
	}
}

class IOBase(DataExchangeable, Unit)
{
	def __init__(self)
	{
		DataExchangeable.__init__(self, None, None)

		self.ctrlIO : AbstractIOController = None
	}

	class IOData(Mutable)
	{
		def __init__(self, io)
		{
			Mutable.__init__(self, io)
			if(isinstance(io, DIO))
			{
				self.value: bool = false
			}
			else
			{
				self.value: float = 0.0
			}
		}

		def read(self)
		{
			self.mutex.lock()
			self.value = self.instance.get()
			self.mutex.unlock()
		}

		def write(self)
		{
			self.mutex.lock()
			if(isinstance(self.instance, DIO_OUT))
			{
				self.instance : DIO_OUT = self.instance #typehint
				self.instance.set(self.value)
			}

			if(isinstance(self.instance, AIO_OUT))
			{
				self.instance : AIO_OUT = self.instance #typehint
				self.instance.set(self.value)
			}
			self.mutex.unlock()
		}
	}

	class IOCommand(DataExchangeable.ExMsgData)
	{
		def __init__(self, data)
		{
			DataExchangeable.ExMsgData.__init__(self, data)
		}
	}

	class IOCommandSet(IOCommand)
	{
		def __init__(self, value)
		{
			IOBase.IOCommand.__init__(self, value)
		}
	}

	def _setDataMsg(self, data: ExMsgData)
    {
		if(isinstance(data, IOBase.IOCommandSet))
        {
			if(isinstance(self, DIO_OUT))
			{
				self.set(data.data)
			}

			if(isinstance(self, AIO_OUT))
			{
				self.set(data.data)
			}
        }

		if(!isinstance(data, IOBase.IOCommand))
		{
			DataExchangeable._setDataMsg(self, data)
		}
    }

	def _getDataMsg(self)
	{
		return IOBase.IOData(self)
	}
}

class DIO(IOBase)
{
}

class AIO(IOBase)
{
}

class DIO_IN(DIO)
{
	def __init__(self, index: int)
	{
		DataExchangeable.__init__(self, None, (DIO_IN, index))

		self.index = index
	}

	def get(self)
	{
		if(self.ctrlIO.switch != None)
		{
			if(self.ctrlIO.switch.get() == "virtual")
			{
				return false
			}
		}
		
		return self.ctrlIO.getDigital(self.index)
	}
}

class DIO_OUT(DIO)
{
	def __init__(self, index: int)
	{
		DataExchangeable.__init__(self, None, (DIO_OUT, index))

		self.index = index
		self.value = false
	}

	def set(self, value: bool)
	{
		if(self.ctrlIO.switch != None)
		{
			if(self.ctrlIO.switch.get() == "virtual")
			{
				return None
			}
		}
		
		self.ctrlIO.setDigital(self.index, value)
	}
	def get(self)
	{
		if(self.ctrlIO.switch != None)
		{
			if(self.ctrlIO.switch.get() == "virtual")
			{
				return false
			}
		}
		
		return self.ctrlIO.getDigitalInternal(self.index)
	}
}

class AIO_IN(AIO)
{
	def __init__(self, index: int)
	{
		DataExchangeable.__init__(self, None, (AIO_IN, index))

		self.index = index
	}

	def get(self)
	{
        if(self.ctrlIO.switch.get() == "virtual")
        {
            return 0.0
        }
		return self.ctrlIO.getAnalog(self.index)
	}
}

class AIO_OUT(AIO)
{
	def __init__(self, index: int)
	{
		DataExchangeable.__init__(self, None, (AIO_OUT, index))

		self.index = index
		self.value = 0.0
	}

	def set(self, value: float)
	{
        if(self.ctrlIO.switch.get() == "virtual")
        {
            return None
        }
		self.ctrlIO.setAnalog(self.index, value)
	}
	def get(self)
	{
        if(self.ctrlIO.switch.get() == "virtual")
        {
            return 0.0
        }
		return self.ctrlIO.getAnalogInternal(self.index)
	}
}

class SLog(Unit)
{
    def __init__(self)
    {
        self.file = SFile()
        self.file.setPath(projectPath())
        self.file.open("testName", "w")
        self.file.write("I am Test Boy !")
    }
}   

class RichActor(FSMActor)
{
	class IdleState(State)
	{
	}

	class MsgJog(UIMessage)
	{
	}

	class MsgJogRelMove(MsgJog)
	{
		def __init__(self, upath: str, pos: float, prfInfo : tuple)
		{
			self.upath = upath
			self.pos = pos
			self.prfInfo = prfInfo
		}
	}

	class MsgCoordMove(UIMessage)
	{
		def __init__(self, upath: str)
		{
			self.upath = upath
		}
	}

	class MsgCoordSet(UIMessage)
	{
		def __init__(self, upath: str)
		{
			self.upath = upath
		}
	}

	def setup(self)
	{
	}


	def __init__(self, name: str)
	{
		FSMActor.__init__(self, name)

       self.uiActor : UIActor = None
       self.dict_data = dict()
		storeman_connect(self.slotSetup)
	}

    def slotSetup(self)
	{
		self.updateAxis()
	}

   	def config(self)
   	{
       	FSMActor.config(self)

		self.updateAxis()
                
        self.addTransition(Transition(FSMActor.MsgNotifyError, None, self.ac_NotifyErrorRemover))
        self.addTransition(Transition(RichActor.MsgJogRelMove, None, self.ac_jogRelMove))
        self.addTransition(Transition(RichActor.MsgCoordMove, None, self.ac_moveCoord))
        self.addTransition(Transition(RichActor.MsgCoordSet, None, self.ac_setCoord))
   	}
        
    def ac_NotifyErrorRemover(self,  state: State, msg: Message, sender: ActorRef) #  for MsgNotifyError Msg remove
    {
		actorName = self.getName()
        return state
    }
    def ac_jogRelMove(self,  state: State, msg: Message, sender: ActorRef)
    {
        listUnit = self.getUnitList(msg.upath)
        tpUnit : tuple = listUnit.get(0)
        
        uAxis : Axis = tpUnit.get(1)
        msg: RichActor.MsgJogRelMove
        
        attrGetter = getattr(self, msg.prfInfo.get(0))
        attrGetter_ = getattr(uAxis, msg.prfInfo.get(1))
        
        uAxis.setProfile(attrGetter_)
        uAxis.relMoveSync(msg.pos)
        return state
    }
    def ac_moveCoord(self,  state: State, msg: Message, sender: ActorRef)
    {
        listUnit = self.getUnitList(msg.upath)
        tpUnit : tuple = listUnit.get(0)
        unit : Variable = tpUnit.get(1)
        
        unit: VariableCoord
        unit.moveSync()
        
        messageBoxText = MutableStr("Move is Done")
        self.callMessageBox(messageBoxText, RichMessageBox.StandardButton.Ok, self.getSelf())
    }
    def ac_setCoord(self,  state: State, msg: Message, sender: ActorRef)
    {
        listUnit = self.getUnitList(msg.upath)
        tpUnit : tuple = listUnit.get(0)
        unit : Variable = tpUnit.get(1)
        
		unit: VariableCoord
		unit.synchronization()
        
		messageBoxText = MutableStr("Set is Done")
		self.callMessageBox(messageBoxText, RichMessageBox.StandardButton.Ok, self.getSelf())
    }    
   	def updateAxis(self)
	{
		varList : RspVarList = self._getVarList(self)
		listCount : int = varList.liPath.count()

		i = 0

		while(i < listCount)
		{
			path : str = varList.liPath.get(i)
			i = i + 1
			unit = self.getUnit(path)

			if(isinstance(unit, VariableCoord))
			{
				unit: VariableCoord
				axisCount = unit._listAxisName.count()

				idx = 0

                cnt2 = unit._listAxis.count()

				unit._listAxis.clear()

				while(idx < axisCount)
				{
					strActor: str = unit._listAxisName.get(idx)
					axis = self.getUnit(strActor)
					idx = idx + 1
					if(isinstance(axis, Axis))
					{
						unit._listAxis.append(axis)
					}
				}
			}
		}
	}

    def _msgHandler(self, msg: Message, sender: ActorRef)   #RichActor
    {
        FSMActor._msgHandler(self, msg, sender)

		useUnit = true
		
		if(isinstance(msg, UIActor.MsgBehaviour))
		{
			msg.behaviour.call()
			
			self.uiActor.tell(msg, self.getSelf())
			
			useUnit = false
		}

		if(isinstance(msg, UIActor.MsgReqAxisList))
		{
			axisList = self._getAxisList()

			self.uiActor.tell(UIActor.MsgRspAxisList(msg, self.getName(), axisList), self.getSelf())

			useUnit = false
		}

        if(isinstance(msg, UIActor.MsgReqAxisDataList))
		{
			axisList = self._getAxisDataList()

			self.uiActor.tell(UIActor.MsgRspAxisDataList(msg, self.getName(), axisList), self.getSelf())

			useUnit = false
		}

		if(isinstance(msg, UIActor.MsgReqIOList))
		{
			ioList = self._getIOList()

			self.uiActor.tell(UIActor.MsgRspIOList(msg, self.getName(), ioList), self.getSelf())

			useUnit = false
		}
		
		if(useUnit)
		{
			listUnit = list()

			if(isinstance(msg, UIActor.MsgSubscribe))
			{
				listUnit = self.getUnitList(msg.upath)
			}

			if(isinstance(msg, UIActor.MsgContribute))
			{
				listUnit = self.getUnitList(msg.upath)
			}
		
			if(isinstance(msg, UIActor.MsgReqData))
			{
				listUnit = self.getUnitList(msg.upath)
			}		

			count = listUnit.count()
			i = 0

			while(i < count)
			{
				tpUnit : tuple = listUnit.get(i)
				i = i + 1

				unit : Variable = tpUnit.get(1)

				if(isinstance(msg, UIActor.MsgSubscribe))   #Subscribe
				{
					unit.signalPublish.connect(self.slotPublish)
					self.dict_data.set(unit, msg.upath)

					if(isinstance(unit, VariableMaterial))
					{
						unit: VariableMaterial
						dataType : DataExchangeable.ExMsgMeta = unit._getMetaMsg()
						dataType.upath = msg.upath
						dataType.childUpath = tpUnit.get(0)
						dataType.liLayer = unit.listLayer()
						unit._publish(dataType)

						initData = unit.__cube._getDataMsg()
                        unit._publish(initData)

						initData = unit.__exist._getDataMsg()
						unit._publish(initData)
					}
					else
					{
						if(isinstance(unit, Package))
						{
							unit.register()
						}
						
						dataType : DataExchangeable.ExMsgMeta = unit._getMetaMsg()
						dataType.upath = msg.upath
						dataType.childUpath = tpUnit.get(0)
						unit._publish(dataType)

						initData = unit._getDataMsg()
						unit._publish(initData)
					}

					varList = self._getVarList(unit)
					unit._publish(varList)
				}

				if(isinstance(msg, UIActor.MsgContribute))
				{
					msg: UIActor.MsgContribute
					data: DataExchangeable.AbstractExMsg = msg.data
					
					unit._contribute(data)
				}
				
				if(isinstance(msg, UIActor.MsgReqData))
				{
					data = unit._getDataMsg()
					
					self.uiActor.tell(UIActor.MsgRspData(msg, self.getName(), data), self.getSelf())
				}
			}
		}
	}

	def ioDataRead(self, dictData: dict)
	{
	}

	def axisDataRead(self, dictData: dict)
	{
	}

    def slotPublish(self, data: DataExchangeable.AbstractExMsg, sender)
    {
        upath : str = self.dict_data.get(sender)
		data.upath = upath
        if(self.uiActor != None)
		{
            self.uiActor.tell(UIActor.MsgPublish(self.getName(), upath, data), self.getSelf())
		}
    }

    def _getVarList(self, var) -> RspVarList
    {
        varList = RspVarList()

        attrs = vars(var)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, Variable))
            {
                attrName = keys.get(i)
                varList.liPath.append(attrName)
            }
            i = i + 1
        }

        return varList
    }

	def _getAxisList(self)
	{
		axisList = RspVarList()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, Axis))
            {
                attrName = keys.get(i)
                axisList.liPath.append(attrName)
            }

            i = i + 1
        }

        return axisList
	}

    def _getAxisDataList(self)
	{
		axisList = RspVarList()

        attrs = vars(self)
        values = attrs.values()
        if(values == None)
        {
            return axisList
        }
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, Axis))
            {
                attrName = keys.get(i)
                axisList.liData.append(attr)
                axisList.liPath.append(attrName)
            }

            i = i + 1
        }

        return axisList
	}

	def _getIOList(self)
	{
		ioList = RspVarList()

        attrs = vars(self)
        values = attrs.values()
        keys = attrs.keys()
        size = values.count()

        i = 0

        while(i < size)
        {
            attr = values.get(i)

            if(isinstance(attr, IOBase))
            {
                attrName = keys.get(i)
                ioList.liPath.append(attrName)
            }

            i = i + 1
        }

        return ioList
	}

	def callMessageBox(self, data , type : int, sender : ActorRef)
	{
		self.bufferMailbox.clearMessageBox()
		uuid = uuid_gen()
		self.uiActor.tell(UIActor.MsgCallMessageBox(uuid, type, data), self.getSelf())
		return uuid
	}
	def callMessageBoxWithUUid(self, data, type : int, uuid : str, sender : ActorRef )
	{
		if(uuid == "")
		{
			uuid = uuid_gen()
		}
		self.uiActor.tell(UIActor.MsgCallMessageBox(uuid, type, data), self.getSelf())
		return uuid
	}
    def callBusyBox(self, type : bool)
    {
        uuid = uuid_gen()
        self.uiActor.tell(UIActor.MsgCallBusyBox(uuid, type), self.getSelf())
        return uuid
    }
    def callNumpadBox(self, min:int, max:int, default:int)
    {
        self.uiActor.tell(UIActor.MsgCallNumpadBox(min, max, default), self.getSelf())
    }

	def closeMessageBox(self, uuid: str)
	{
		self.uiActor.tell(UIActor.MsgCloseMessageBox(uuid), self.getSelf())
	}
}

class TCPClient(DataExchangeable, Unit)
{
	def __init__(self)
	{
		DataExchangeable.__init__(self, None, None)
	}

	def readyRead(self)
	{
	}

	def connect(self, ip: str, port: int)
	{
		self.socket = STcpSocket()
		self.socket.connect(ip, port)
		self.socket.readyRead.connect(self.readyRead)
	}

	def close(self)
	{
		self.socket.close()
	}

	def write(self, data: str)
	{
		self.socket.write(data)
	}

	def readAll(self)
	{
		return self.socket.readAll()
	}
}

class SerialPort(DataExchangeable, Unit)
{
	class BaudRate()
	{
		Baud1200 = 1200
        Baud2400 = 2400
        Baud4800 = 4800
        Baud9600 = 9600
        Baud19200 = 19200
        Baud38400 = 38400
        Baud57600 = 57600
        Baud115200 = 115200
	}

	class DataBits()
	{
		Data5 = 5
        Data6 = 6
        Data7 = 7
        Data8 = 8
	}

	class Parity()
	{
		NoParity = 0
        EvenParity = 2
        OddParity = 3
        SpaceParity = 4
        MarkParity = 5
	}

	class StopBits()
	{
		OneStop = 1
        OneAndHalfStop = 3
        TwoStop = 2
	}

	class FlowControl()
	{
		NoFlowControl = 0
        HardwareControl = 1
        SoftwareControl = 2
	}

	def __init__(self)
	{
		DataExchangeable.__init__(self, None, None)
        self.serial = SSerialPort()
	}

	def open(self, com: int, baudRate: BaudRate, dataBits: DataBits, parity: Parity, stopBits: StopBits, flowControl: FlowControl)
	{
		bSuccess = self.serial.open(com, baudRate, dataBits, parity, stopBits, flowControl)
		return bSuccess
	}

    def connectWithReadyRead(self, slot : function)
    {
        self.serial.readyRead.connect(slot)
    }
	def connectWithReadyReadNewLine(self, slot : function)
	{	
		self.serial.readyReadNewLine.connect(slot)
	}
	
	def close(self)
	{
		self.serial.close()
	}

	def clear(self)
	{
		self.serial.clear()
	}	
	
	def write(self, data: str)
	{
		self.serial.write(data)
	}
    def setNewLine(self, newLine : str)
    {
        self.serial.setNewLine(newLine)
    }
	def readLine(self)
	{	
		return self.serial.readLine()
	}
	def getBufferLength(self)
    {
        return self.serial.getBufferLength()
    }
	def readAll(self)
	{
		return self.serial.readAll()
	}
}

class ScaleController(Unit)
{
	def __init__(self)
	{
        self.serial = SSerialPort()
        self.data = None
        self.dataReceiveDone = false
        self.mutex = SMutex()
	}
    def open(self, com: int, baudRate: BaudRate, dataBits: DataBits, parity: Parity, stopBits: StopBits, flowControl: FlowControl)
    {
        bSuccess = self.serial.open(com, baudRate, dataBits, parity, stopBits, flowControl)
		if(bSuccess)
		{	
			print("Connect Succes !")	
		}
		else
		{	
			print("Connect Fail !")
		}
        self.serial.readyRead.connect(self.slotReadyRead)
		return bSuccess
    }
    def setReceiveDone(self, value: bool)
    {
        self.mutex.lock()
        self.dataReceiveDone = value
        self.mutex.unlock()
    }
    def getReceiveDone(self)
    {
        self.mutex.lock()
        res = self.dataReceiveDone
        self.mutex.unlock()
        return res
    }
    def slotReadyRead(self)
    {
		print("Ready Read!")
        self.setReceiveDone(true)
		self.data = self.serial.readAll()
    }
    def close(self)
	{
		self.serial.close()
	}
	def write(self, data: str)
	{
		self.serial.write(data)
	}
	def readAll(self)
	{
		print("receive Done : ", self.getReceiveDone())
		while(true)
		{
	        if(self.getReceiveDone())
	        {
	            res = self.data
	            self.setReceiveDone(false)
	            return res
	        }
		}
		msleep(1)
	}
}

class LoadCellController(ScaleController)
{
	def __init__(self)
	{
        ScaleController.__init__(self)
		result = self.open(15, 9600, 8, 0, 1, 0)
	}
    def getCurrentValue(self)
    {
        self.write("ID01P")
        return self.readAll()
    }
    def setZero(self)
    {
        self.write("1D01Z")
    }
}

class Package(Unit, DataExchangeable)
{
	def __init__(self)
	{
		DataExchangeable.__init__(self, None, None)
		
		self.listVariable = list()
	}
	
	def register(self)
	{
		attrs = vars(self)
		sortedItem = attrs.sortedItems()
		
		for i in range(sortedItem.count())
		{
			tpItem = sortedItem.get(i)
			attr = tpItem.get(1)
			
			if(isinstance(attr, VariableSingle))
			{
				if(hasattr(attr, "desc"))
				{
					attr.signalPublish.connect(self.slotPublish)
					self.listVariable.append(tpItem)
				}
			}
		}
	}
	
	def _getMetaMsg(self) -> ExMsgMeta
    {
        meta = DataExchangeable.ExMsgMeta(self.typeContainer)
		meta.length = self.listVariable.count()
		
		for i in range(meta.length)
		{
			tpItem = self.listVariable.get(i)
			vs = tpItem.get(1)

            if(hasattr(vs, "desc"))
			{
				meta.li.append(vs.desc)
			}
		}

        return meta
    }
	
	def _getDataMsg(self)
	{
		listData = list()
		
		for i in range(self.listVariable.count())
		{
			tpItem = self.listVariable.get(i)
			vs = tpItem.get(1)
			
			listData.append(vs.data)
		}
		
		msg = DataExchangeable.ExMsgData(listData)
		
		return msg
	}
	
	def _contribute(self, value: DataExchangeable.AbstractExMsg)
    {
        if(isinstance(value, DataExchangeable.ExMsgData))
        {
			value: DataExchangeable.ExMsgData
			
			if(value.idx >= 0 and value.idx < self.listVariable.count())
			{
				tpItem = self.listVariable.get(value.idx)
				vs = tpItem.get(1)
				vs._setDataMsg(value)
			}
        }
    }
	
	def slotPublish(self, data: AbstractExMsg, sender)
    {
		idx = -1
		
		for i in range(self.listVariable.count())
		{
			tpItem = self.listVariable.get(i)
			vs = tpItem.get(1)
			
			if(vs == sender)
			{
				idx = i
				break
			}
		}
		
		if(idx != -1)
		{
			data.idx = idx
			self.signalPublish.emit(data, self)
		}
    }
}

class VisionController(Unit)
{
    class EVisionState()	
	{
		NONE = 0
		TRIGGER = 1
		GRABEND = 2
	}
	def __init__(self , camCount : int)
	{
		self.dateTime = DateTime()
        self.tcpVision = STcpSocket()  
        self.list_VisionData  = list()
	}
	def getState(self)
	{	
		return self.tcpVision.getState()
	}

    def connect(self, ip : str , port : int)
    {
        visionState = self.tcpVision.getState()
        if(visionState != TCPSocketState.ConnectedState)	
        {
            self.tcpVision.connect(ip, port)
        }
    }
	def isValid(self)
	{	
		return self.tcpVision.isValid()
	}
    def waitForConnected(self, msec : int)
    {
        return self.tcpVision.waitForConnected(msec)
    }
    def trigger(self, camIndex : int)
    {
        # implemented in the inherited classes
        return None
    }
    def jobChange(self, camIndex : int)
    {
        # implemented in the inherited classes
        return None
    }
    def inspChange(self, camIndex : int, inspIndex : int, inspMode : int)
    {
        # implemented in the inherited classes
        return None
    }
    def inspChange(self, camIndex : int, inspIndex : int, inspMode : int)
    {
        # implemented in the inherited classes
        return None
    }
    def hide(self, isHide : bool)
    {
        # implemented in the inherited classes
        return None
    }
    def saveImage(self, camIndex : int, shotNumber : int, fileName : str)
    {
        # implemented in the inherited classes
        return None
    }
    def calibration(self, camIndex : int, realDistanceX : int, realDistanceY : int)
    {
       # implemented in the inherited classes
        return None
    }
    def write(self, msgName : str, msg : str)
    {
        # implemented in the inherited classes
        return None
    }
    def setReceiveDone(self, camIndex : int)
    {
        # implemented in the inherited classes
        return None
    }
    def waitResult(self, camIndex: int)
    {
        # implemented in the inherited classes
        return None
    }
}
class ProtecVisionController(VisionController)
{
    class VisionData()
    {
        def __init__(self)
        {
            self.sMsg = ""
            self.nState = -1
            self.spfXY = SPointF(0.0, 0.0)
            self.fAngle = 0
        }
    }
    def __init__(self, camIndex : int)
    {
        VisionController.__init__(self, camIndex)
        self.mutex = SMutex()
        self.listReceiveDone = list()
        self.camCount = camIndex
        for i in range(camIndex)
        {
            self.listReceiveDone.append(false)
            self.list_VisionData.append(None)
        }
        self.STX = chr(2)
        self.ETX = chr(3)
        self.tcpVision.readyRead.connect(self.slotReadyRead)
    }
    def slotReadyRead(self)
    {
        temp = self.tcpVision.readAll()
        self.parse(temp)
    }
    def trigger(self, camIndex : int)
    {
        self.write("Trigger", str(camIndex) + ";")
    }
    def jobChange(self, camIndex : int, name : str)
    {
        self.write("JobChange", str(camIndex) + ";" + name + ";")
    }
    def inspChange(self, camIndex : int, inspIndex : int, inspMode : int)
    {
        self.write("InspChange", str(camIndex) + ";" + str(inspIndex) + ";" + str(inspMode) + ";" )
    }
    def setShowMode(self, option : int)
    {
        self.write("SetShowMode", str(option) + ";")
    }
    def hide(self, isHide : bool)
    {
        isHideOption = "0;"
        if(!isHide)
        {
            isHideOption = "1;"
        }
        self.write("Hide", isHideOption)
    }
    def saveImage(self, camIndex : int, shotNumber : int, fileName : str)
    {
        self.write("SaveImage", str(camIndex) + ";" + str(shotNumber) + ";" + filename + ";")
    }
    def calibration(self, camIndex : int, realDistanceX : int, realDistanceY : int)
    {
        self.write("Calibration", str(camIndex) + ";" + str(realDistanceX) + ";" + str(realDistanceY) + ";")
    }
    def write(self, msgName : str, msg : str)
    {
        str_msg = msg
		strList = str_msg.split(";")
		total_msg = ""
		P_Type = "O"
		Command = "SCR"
		C_Type = "001"
		Data_Length = "0001"
		Data = ""
		if(msgName == "Trigger")	
		{
			camIndex = strList.get(0)
			Command = "SGI"
			Data = camIndex + ";1;0"
			#self.list_trigger.set(camIndex, self.EVisionState.TRIGGER)
		}
		elif(msgName == "JobChange")	
		{
			Command = "SCR"
			camIndex = strList.get(0)
            jobName = strList.get(1)
			Data = str_msg
		}
		elif(msgName == "InspChange")	
		{
            Command = "SCI"    
			camIndex = strList.get(0)
			insp = strList.get(1)
			mode = strList.get(2)
			Data = str_msg
		}
		elif(msgName == "SetShowMode")	
		{
			Command = "SSM"
			Data = str_msg
		}
		elif(msgName == "Hide")	
		{
			Command = "SWV"
			Data = str_msg
		}
		elif(msgName == "SaveImage")	
		{
			Command = "SLI"
			Data = str_msg
		}
		elif(msgName == "Calibration")	
		{
			Command = "SMC"
			Data = str_msg
		}
        
		if(len(Data) < 10)	
		{
			Data_Length = "000" + str(len(Data))
		}
		elif(len(Data) < 100)	
		{
			Data_Length = "00" + str(len(Data))
		}
		elif(len(Data) < 1000)	
		{
			Data_Length = "0" + str(len(Data))
		}
        
		total_msg = self.STX + P_Type + Command + C_Type + Data_Length + Data + self.ETX
		
        print("")        
		print("[" + self.dateTime.currentTime_ms() + "]", "--Send Message : ", total_msg) 
		
        self.tcpVision.write(total_msg)
    }
    def setVisionData(self, camIndex : int, visionData : VisionData)
    {
        self.list_VisionData[camIndex] = visionData
    }
    def setReceiveDone(self, camIndex : int)
    {
        self.mutex.lock()
        self.listReceiveDone[camIndex] = true
        self.mutex.unlock()
    }
    def getReceiveDone(self, camIndex : int)
    {
        self.mutex.lock()
        res = self.listReceiveDone[camIndex]
        self.mutex.unlock()
        return res
    }   
    def waitResult(self, camIndex : int, msec : int)
    {
        if(self.tcpVision.getState() == 0)
        {
            return ProtecVisionController.VisionData()
        }
        waitTimer = SElapsedTimer()
        waitTimer.start()
        resVisionData = None
        while(true)
        {
            if(waitTimer.elapsed() > msec)
            {
				return None
            }
            if(self.getReceiveDone(camIndex))
            {
                resVisionData = self.list_VisionData[camIndex]
				self.setReceiveDone(false)
                return resVisionData
            }
        }
    }
    def parse(self, readMsg : str)	
    { 
        bFake = true
        list_str = readMsg.split(self.STX)
        if(list_str.count() > 1)
        {
            list_str = list_str.get(1).split(self.ETX)
            bFake = false
        }
        msg = list_str.get(0)
               
        camIndexStr = "999" # no camIndex Num
        num = 0
       
        print("[" + self.dateTime.currentTime_ms() + "]", "--Receive Msg : ",  msg)
       
        P_Type = msg.substr(num, 1)
        num = num + 1 
        Command = msg.substr(num, 3)
        num = num + 3
        C_Type = msg.substr(num, 3)
        num = num + 3
        Data_Length = msg.substr(num, 4)
        num = num + 4
         
       # print("P-Type : ", P_Type)
       # print("Command : ", Command)
       # print("C-Type : ",C_Type)
       # print("DataLength : ", Data_Length)
        if(int(Data_Length) > 0)
        {
            Data = msg.substr(num, num + int(Data_Length))
           # print("Data : ", Data)
        }
        
        if (Command == "SGI")    # SGI Send
        {   
            if(C_Type == "002")
            {
                list_data = Data.split(";")
                camIndexStr = list_data.get(1)
                visiondata = ProtecVisionController.VisionData()
                visiondata.sMsg = msg
                visiondata.nState = list_data.get(0)
                self.setVisionData(int(camIndexStr), visiondata)
            }
            elif(C_Type == "003")
            {
                camIndexStr = msg.substr(num,1)
                camIndex = int(camIndexStr)
				#print("cam INDEX : ", camIndex)
                visiondata = ProtecVisionController.VisionData()
                list_data = Data.split(";")
                visiondata.camIndex = camIndex
                visiondata.sMsg = msg
                visiondata.nState = list_data.get(0)
               # resultStrList = list_data.get(3).split(",")
                r_x = list_data.get(1)
                r_y = list_data.get(2)
                r_a = list_data.get(3)
				f_r_x = float(r_x)
				f_r_y = float(r_y)
                visiondata.spfXY = SPointF(f_r_x,f_r_y)
                visiondata.fAngle = float(r_a)
                self.setVisionData(camIndex, visiondata)     
                self.setReceiveDone(camIndex) # SGI 003 Receive Done Flag On
            }
        }
        elif (Command == "SGE")   
        {                        
            camIndexStr = msg.substr(num,1)
        }
        elif(Command == "SCI")
        {       
            list_data = Data.split(";")
            if(list_data.count() > -1)
            {
                camIndexStr = list_data.get(list_data.count() - 1)
            }
        }     
    }
}

class MotionControllerAdapter(AbstractMotionController)
{
	def __init__(self, name: str)
	{
		AbstractMotionController.__init__(self, name)
		self.switch: VariableSingle = None
	}

	def getMyMotionController(self) -> AbstractMotionController
	{
		curUnit = self

		if(self.switch != None)
		{
			if(hasattr(curUnit, self.switch.get()))
			{
				myMotion : AbstractMotionController = getattr(curUnit, self.switch.get())
				return myMotion
			}
		}
		return None
	}

	def terminate(self)
	{

	}

	def setName(self, axis: int, name: str)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setName(axis, name)
		}
	}

	def isAlarm(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.isAlarm(axis)
		}
	}

	def enable(self, axis: int, enable: bool)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.enable(axis, enable)
		}
	}

	def initMotor(self, axis: int, nOption: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.initMotor(axis, nOption)
		}
	}

	def isEnabled(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.isEnabled(axis)
		}
		print("can not find motionCtrl")
		assert(false)
		return false
	}

	def moveSync(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.moveSync(axis, pos)
		}
	}

	def relMove(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.relMove(axis, pos)
		}
	}

	def velMove(self, axis: int, reverse: bool)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.velMove(axis, reverse)
		}
	}

	def move(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.move(axis, pos)
		}
	}

	def relMoveSync(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.relMoveSync(axis, pos)
		}
	}

	def isMoving(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.isMoving(axis)
		}
		print("can not find motionCtrl")
		assert(false)
		return false
	}

	def getCmdPos(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.getCmdPos(axis)
		}
		print("can not find motionCtrl")
		assert(false)
		return 0.0
	}

	def getActPos(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.getActPos(axis)
		}
		print("can not find motionCtrl")
		assert(false)
		return 0.0
	}

	def refreshTarget(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.refreshTarget(axis)
		}
	}

	def setTarget(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setTarget(axis)
		}
	}

	def stop(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.stop(axis)
		}
	}

	def abort(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.abort(axis)
		}
	}

	def ampFault(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.ampFault(axis)
		}
	}

	def release_cmd(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.motion_release_cmd(axis)
		}
	}

	def setPosition(self, axis: int, pos: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setPosition(axis, pos)
		}
	}

	def setAccel(self, axis: int, value: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setAccel(axis, value)
		}
	}

	def setDecel(self, axis: int, value: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setDecel(axis, value)
		}
	}

	def setJerk(self, axis: int, value: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setJerk(axis, value)
		}
	}

	def setVelocity(self, axis: int, value: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.setVelocity(axis, value)
		}
	}

    def setSpeedPattern(self, axis : int, mode : int, workSpeed : float,  accel : float, decel : float)
    {
        myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
            if(myController.name == "comizoa")
            {
                myController.setSpeedPattern(axis, mode, workSpeed, accel,  decel)
            }
		}
        else
        {
            print("setSpeedPattern FAIL")
        }
    }

	def clear(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.clear(axis)
		}
	}

	def panic(self)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			myController.panic()
		}
	}

	def getLimitNStatus(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.getLimitNStatus(axis)
		}
	}

	def getLimitPStatus(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.getLimitPStatus(axis)
		}
	}

	def getHomeStatus(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.getHomeStatus(axis)
		}
	}

	def ClearSuperviser(self, axis1: int, axis2: int, union_axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.ClearSuperviser(axis1, axis2, union_axis)
		}
	}

	def find_z_phase1(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.find_z_phase1(mode, axis, pls_rev, vel, acc, jerk)
		}
	}

	def find_z_phase2(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.find_z_phase2(mode, axis, pls_rev, vel, acc, jerk)
		}
	}

	def find_z_phase3(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.find_z_phase3(mode, axis, pls_rev, vel, acc, jerk)
		}
	}

	def find_z_phase4(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.find_z_phase4(mode, axis, pls_rev, vel, acc, jerk)
		}
	}

	def moveSeq(self, axis: int, pos1: float, vel1: float, acc1: float, jerk1: float, pos2: float, vel2: float, acc2: float, jerk2: float)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.moveSeq(axis, pos1, vel1, acc1, jerk1, pos2, vel2, acc2, jerk2)
		}
	}

	def moveSeq_Touch(self, axis1: int, pos1: float, vel1: float, acc1: float, jerk1: float, pos2: float, vel2: float, acc2: float, jerk2: float, axis_enc: int, encoder_targer: float, bUseGaninTable: bool)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.moveSeq_Touch(axis, pos1, vel1, acc1, jerk1, pos2, vel2, acc2, jerk2, axis_enc, encoder_targer, bUseGaninTable)
		}
	}

	def AutoLevel_SpdMode(self, axis: int, vel: float, acc: float, jerk: float, axis_enc: int, encoder_targer: float, bUseGaninTable: bool)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController.AutoLevel_SpdMode(axis, vel, acc, jerk, axis_enc, encoder_targer, bUseGaninTable)
		}
	}
	def _SequenceStop(self, axis: int)
	{
		myController : AbstractMotionController = self.getMyMotionController()
		if( myController != None)
		{
			return myController._SequenceStop(axis)
		}
	}
}

class VirtualMotionController(AbstractMotionController)
{
	def __init__(self, name: str)
	{
		AbstractMotionController.__init__(self, name)
		self.initialize(name)
	}

	def initialize(self, name: str)
	{
		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\VirtualDriver_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\VirtualDriver_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\VirtualDriver_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Release\\VirtualDriver_32.dll")
			}
		}

		self.myDll.loadProc("motion_open")
		self.myDll.motion_open.restype(c_int())
		self.myDll.motion_open.argtypes(c_string())

		self.myDll.loadProc("motion_setName")
		self.myDll.motion_setName.argtypes(c_int(), c_int(), c_string())

		self.myDll.loadProc("motion_isAlarm")
		self.myDll.motion_isAlarm.restype(c_bool())
		self.myDll.motion_isAlarm.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_enable")
		self.myDll.motion_enable.argtypes(c_int(), c_int(), c_bool())

		self.myDll.loadProc("motion_isEnabled")
		self.myDll.motion_isEnabled.restype(c_bool())
		self.myDll.motion_isEnabled.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_move")
		self.myDll.motion_move.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_relMove")
		self.myDll.motion_relMove.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_isMoving")
		self.myDll.motion_isMoving.restype(c_bool())
		self.myDll.motion_isMoving.argtypes(c_int(), c_int())

		self.myDll.loadProc("_getCommand")
		self.myDll._getCommand.restype(c_double())
		self.myDll._getCommand.argtypes(c_int(), c_int())

		self.myDll.loadProc("_getActual")
		self.myDll._getActual.restype(c_double())
		self.myDll._getActual.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_stop")
		self.myDll.motion_stop.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_abort")
		self.myDll.motion_abort.argtypes(c_int(), c_int())

		self.myDll.loadProc("_ampFault")
		self.myDll._ampFault.restype(c_bool())
		self.myDll._ampFault.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_release_cmd")
		self.myDll.motion_release_cmd.argtypes(c_int(), c_int(), c_int())

		self.myDll.loadProc("motion_setPosition")
		self.myDll.motion_setPosition.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setAccel")
		self.myDll.motion_setAccel.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setDecel")
		self.myDll.motion_setDecel.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setJerk")
		self.myDll.motion_setJerk.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setVelocity")
		self.myDll.motion_setVelocity.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_clear")
		self.myDll.motion_clear.argtypes(c_int(), c_int())

		self.id = self.myDll.motion_open.call(name)
	}

	def terminate(self)
	{
	}

	def initMotor(self, axis: int, nOption: int)
	{
	}

	def setName(self, axis: int, name: str)
	{
		self.myDll.motion_setName.call(self.id, axis, name)
	}

	def isAlarm(self, axis: int)
	{
		return self.myDll.motion_isAlarm.call(self.id, axis)
	}

	def enable(self, axis: int, enable: bool)
	{
		self.myDll.motion_enable.call(self.id, axis, enable)
	}

	def isEnabled(self, axis: int)
	{
		return self.myDll.motion_isEnabled.call(self.id, axis)
	}

	def moveSync(self, axis: int, pos: float)
	{
		self.myDll.motion_move.call(self.id, axis, pos)
		self.wait(axis)
	}

	def relMove(self, axis: int, pos: float)
	{
		self.myDll.motion_relMove.call(self.id, axis, pos)
	}

	def move(self, axis: int, pos: float)
	{
		self.myDll.motion_move.call(self.id, axis, pos)
	}

	def relMoveSync(self, axis: int, pos: float)
	{
		self.myDll.motion_relMove.call(self.id, axis, pos)
		self.wait(axis)
	}

	def isMoving(self, axis: int)
	{
		return self.myDll.motion_isMoving.call(self.id, axis)
	}

	def getCmdPos(self, axis: int)
	{
		return 0
		#return self.myDll._getCommand.call(self.id, axis)
	}

	def getActPos(self, axis: int)
	{
		return 0
		#return self.myDll._getActual.call(self.id, axis)
	}

	def stop(self, axis: int)
	{
		self.myDll.motion_stop.call(self.id, axis)
	}

	def abort(self, axis: int)
	{
		self.myDll.motion_abort.call(self.id, axis)
	}

	def ampFault(self, axis: int)
	{
		return self.myDll._ampFault.call(self.id, axis)
	}

	def release_cmd(self, axis: int)
	{
		return self.myDll.motion_release_cmd.call(self.id, axis)
	}

	def setPosition(self, axis: int, pos: float)
	{
		self.myDll.motion_setPosition.call(self.id, axis, pos)
	}

	def setAccel(self, axis: int, value: float)
	{
		self.myDll.motion_setAccel.call(self.id, axis, value)
	}

	def setDecel(self, axis: int, value: float)
	{
		self.myDll.motion_setDecel.call(self.id, axis, value)
	}

	def setJerk(self, axis: int, value: float)
	{
		self.myDll.motion_setJerk.call(self.id, axis, value)
	}

	def setVelocity(self, axis: int, value: float)
	{
		self.myDll.motion_setVelocity.call(self.id, axis, value)
	}

	def clear(self, axis: int)
	{
		self.myDll.motion_clear.call(self.id, axis)
	}

	def getHomeStatus(self, axis: int)
	{
		return true
	}

	def panic(self)
	{
	}
}

class COMIZOAController(AbstractMotionController, AbstractIOController)
{
    def __init__(self, name: str)
    {
    	AbstractMotionController.__init__(self, name)
		AbstractIOController.__init__(self, name)
        self.numOfAxes = 0
		self.initialize()
    }
    
    def initialize(self)
	{
		#Only 32bit
        if(isBuildDebug())
        {
            self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\COMIZOA.dll")
        }
        else
        {
            self.myDll = ctypes_cdll("COMIZOA.dll")
        }
        
        self.myDll.loadProc("_cmmLoadDll")
		self.myDll._cmmLoadDll.restype(c_bool())
        
        self.myDll.loadProc("_cmmGnDeviceLoad")
        self.myDll._cmmGnDeviceLoad.restype(c_long())
        self.myDll._cmmGnDeviceLoad.argtypes(c_bool(), c_pointer(c_long()))
        
        self.myDll.loadProc("_cmmGnDeviceIsLoaded")
        self.myDll._cmmGnDeviceIsLoaded.restype(c_long())
        self.myDll._cmmGnDeviceIsLoaded.argtypes(c_pointer(c_long()))
        
        self.myDll.loadProc("_cmmGnSetEmergency")
        self.myDll._cmmGnSetEmergency.restype(c_long())
        self.myDll._cmmGnSetEmergency.argtypes(c_bool(), c_bool())
        
        self.myDll.loadProc("_cmmGnSetAlarmRes")
        self.myDll._cmmGnSetAlarmRes.restype(c_long())
        self.myDll._cmmGnSetAlarmRes.argtypes(c_long(), c_bool())
        
        self.myDll.loadProc("_cmmGnGetAlarmRes")
        self.myDll._cmmGnGetAlarmRes.restype(c_long())
        self.myDll._cmmGnGetAlarmRes.argtypes(c_long(), c_pointer(c_long()))
        
        self.myDll.loadProc("_cmmCfgSetMioProperty")
        self.myDll._cmmCfgSetMioProperty.restype(c_long())
        self.myDll._cmmCfgSetMioProperty.argtypes(c_long(), c_long(), c_bool())
        
        self.myDll.loadProc("_cmmGnSetServoOn")
        self.myDll._cmmGnSetServoOn.restype(c_long())
        self.myDll._cmmGnSetServoOn.argtypes(c_long(), c_bool())
        
        self.myDll.loadProc("_cmmGnGetServoOn")
        self.myDll._cmmGnGetServoOn.restype(c_long())
        self.myDll._cmmGnGetServoOn.argtypes(c_long(), c_bool())
        
        self.myDll.loadProc("_cmmCfgSetSpeedPattern")
        self.myDll._cmmCfgSetSpeedPattern.restype(c_long())
        self.myDll._cmmCfgSetSpeedPattern.argtypes(c_long(), c_long(), c_double(), c_double(), c_double())
        
        self.myDll.loadProc("_cmmSxSetSpeedRatio")
        self.myDll._cmmSxSetSpeedRatio.restype(c_long())
        self.myDll._cmmSxSetSpeedRatio.argtypes(c_long(), c_long(), c_double(), c_double(), c_double())
        
        self.myDll.loadProc("_cmmSxMove")
        self.myDll._cmmSxMove.restype(c_long())
        self.myDll._cmmSxMove.argtypes(c_long(), c_double(), c_bool())
        
        self.myDll.loadProc("_cmmSxMoveStart")
        self.myDll._cmmSxMoveStart.restype(c_long())
        self.myDll._cmmSxMoveStart.argtypes(c_long(), c_double())
        
        self.myDll.loadProc("_cmmSxMoveTo")
        self.myDll._cmmSxMoveTo.restype(c_long())
        self.myDll._cmmSxMoveTo.argtypes(c_long(), c_double(), c_bool())
        
        self.myDll.loadProc("_cmmSxMoveToStart")
        self.myDll._cmmSxMoveToStart.restype(c_long())
        self.myDll._cmmSxMoveToStart.argtypes(c_long(), c_double())
        
        self.myDll.loadProc("_cmmLtcIsLatched")
        self.myDll._cmmLtcIsLatched.restype(c_long())
        self.myDll._cmmLtcIsLatched.argtypes(c_long(), c_pointer(c_long()))
  
        
        self.myDll.loadProc("_cmmLtcReadLatch")
        self.myDll._cmmLtcReadLatch.restype(c_long())
        self.myDll._cmmLtcReadLatch.argtypes(c_long(), c_pointer(c_long()))
        
        self.myDll.loadProc("_cmmSxStop")
        self.myDll._cmmSxStop.restype(c_long())
        self.myDll._cmmSxStop.argtypes(c_long(), c_long(), c_long())
        
        self.myDll.loadProc("_cmmSxStopEmg")
        self.myDll._cmmSxStopEmg.restype(c_long())
        self.myDll._cmmSxStopEmg.argtypes(c_long())
        
        self.ctrlIO = self.myDll
        
        self.ctrlIO.loadProc("_cmmDiGetOne")
        self.ctrlIO._cmmDiGetOne.restype(c_long())
        self.ctrlIO._cmmDiGetOne.argtypes(c_long(), c_pointer(c_long()))
        
        self.ctrlIO.loadProc("_cmmDoGetOne")
        self.ctrlIO._cmmDoGetOne.restype(c_long())
        self.ctrlIO._cmmDoGetOne.argtypes(c_long(), c_pointer(c_long()))
        
        self.ctrlIO.loadProc("_cmmDoPutOne")
        self.ctrlIO._cmmDoPutOne.restype(c_long())
        self.ctrlIO._cmmDoPutOne.argtypes(c_long(), c_long())
        
        if(self.myDll._cmmLoadDll.call() == true)
        {
            print("COMIZOA LOAD DLL Good")
        }
        if(self.myDll._cmmGnDeviceLoad.call(true, self.numOfAxes) == 0)
        {
            print("COMIZOA DEVICE LOAD Good", "Axes Count : ", self.numOfAxes)
        }
        if(self.myDll._cmmCfgSetMioProperty.call(0, 0, true) == 0)
        {
            # 6층 test 장비 test를 위해 기본 소스코드로 잠깐 추가
            # 0번 Axis Alarm 설정 반전 시키는 소스코드
            print("BUILTIN 8700 LINE, MAIN IO PROPERTY SET FOR TEST")
        }
		#isLatched = 999
		#self.myDll._cmmLtcIsLatched.call(0, isLatched)
		#print("BUILTIN 8731 LINE, isLatched Result : " , isLatched)
        #self.myDll._cmmGnGetAlarmRes.call(0, isLatched)
        #print("BUILTIN 8736 LINE, Alram Result : " , isLatched)
    }
    
    class speedMode()
    {
        cmSMODE_KEEP = -1
        cmSMODE_C = 0
        cmSMODE_T = 1
        cmSMODE_S = 2
    }
    
    #IO_input
    def getDigital(self, idx: int) -> float
    { 
        resultOfDI = false
        self.ctrlIO._cmmDiGetOne.call(idx, resultOfDI)
        return resultOfDI
	}
    
    #IO_output
    def getDigitalInternal(self, idx: int) -> float
	{
        resultOfDO = false
        self.ctrlIO._cmmDoGetOutputLogic.call(idx, resultOfDO)
        return resultOfDO
	}
	def setDigital(self, idx: int, bVal: bool)
	{
        self.ctrlIO._cmmDoPutOne.call(idx, bVal)
	}
        
    def panic(self)
    {
        self.myDll._cmmGnSetEmergency.call(true, false)
    }
    def clear(self, axis : int)
    {
        self.myDll._cmmGnSetAlarmRes.call(axis, false)
    }
	def isAlarm(self, axis : int)
	{
		currentAlramState = 0
        self.myDll._cmmGnGetAlarmRes.call(axis, currentAlramState)
        if(currentAlramState == 0)
        {
            return false
        }
        return true
	}    
	
    def enable(self, axis : int, enable : bool)
    {
        return self.myDll._cmmGnSetServoOn.call(axis, enable)
    }
    
    def relMoveSync(self, axis : int, distance : float)
    {
        print("REL MOVE SYNC BLOCKING IS FALSE NOW BUITIN LINE 8742")
        # 일단은 false로 고정 해둠 test 필요
        return self.myDll._cmmSxMove.call(axis, distance, false)
    }
    
    def relMove(self, axis : int, distance : float)
    {
        return self.myDll._cmmSxMoveStart.call(axis, distance, false)
    }
    
    def moveSync(self, axis : int, distance : float)
    {
        print("REL MOVE SYNC BLOCKING IS FALSE NOW BUITIN LINE 8742")
        # 일단은 false로 고정 해둠 test 필요
        return self.myDll._cmmSxMoveTo.call(axis, distance, false)
    }
    
    def move(self, axis : int, distance : float)
    {
        return self.myDll._cmmSxMoveToStart.call(axis, distance)
    }
    
    def getCmdPos(self, axis: int)
	{
        dblCmdPos = 0.0
		self.myDll._cmmLtcReadLatch.call(axis, 0, dblCmdPos)
		return dblCmdPos
	}
    
    def getActPos(self, axis : int)
    {
        dblCmdPos = 0.0
		self.myDll._cmmLtcReadLatch.call(axis, 1, dblCmdPos)
		return dblCmdPos
    }
    
    def stop(self, axis: int)
	{
		self.myDll._cmmSxStop.call(axis, false, false)
	}

	def abort(self, axis: int)
	{
        self.myDll._cmmSxStopEmg.call(axis)
	}
    
    def ampFault(self, axis : int)
    {
        self.myDll._cmmGnGetServoOn.call(axis)
    }
    
    ######### Only COMIZOA
    def setMainIOProperty(self, axis : int, propId : int, propVal : bool)
    {
        return self.myDll._cmmCfgSetMioProperty.call(axis, propId, propVal)
    }
    def setAlramReset(self, res : bool)
	{	
		self.myDll._cmmGnSetAlarmRes.call(0, true)
	}
    def setSpeedPattern(self, axis : int, mode : int, workSpeed : float,  accel : float, decel : float)
    {
        return self.myDll._cmmCfgSetSpeedPattern.call(axis, mode, workSpeed, accel, decel)
    }
    
    def setSpeedRatio(self, axis : int, mode : int, velRatio : float,  accRatio : float, decRatio : float)
    {
        return self.myDll._cmmSxSetSpeedRatio.call(axis, mode, velRatio, accRatio, decRatio)
    }
}

class MEIController(AbstractMotionController, AbstractIOController)
{
	def __init__(self, name: str, index: int)
	{
		self.id = -1
		AbstractMotionController.__init__(self, name)
		AbstractIOController.__init__(self, name)
		self.initialize(index)
	}

	def initialize(self, index: int)
	{
		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\MEIDriver_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\MEIDriver_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("MEIDriver_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("MEIDriver_32.dll")
			}
		}
		self.myDll.loadProc("motion_open")
		self.myDll.motion_open.restype(c_int())
		self.myDll.motion_open.argtypes(c_int())

		self.myDll.loadProc("motion_close")
		self.myDll.motion_close.argtypes(c_int())

		self.myDll.loadProc("_initMotor")
		self.myDll._initMotor.argtypes(c_int(), c_int(), c_int())

		self.myDll.loadProc("motion_isAlarm")
		self.myDll.motion_isAlarm.restype(c_bool())
		self.myDll.motion_isAlarm.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_enable")
		self.myDll.motion_enable.argtypes(c_int(), c_int(), c_bool())

		self.myDll.loadProc("motion_isEnabled")
		self.myDll.motion_isEnabled.restype(c_bool())
		self.myDll.motion_isEnabled.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_move")
		self.myDll.motion_move.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_relMove")
		self.myDll.motion_relMove.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_velMove")
		self.myDll.motion_velMove.argtypes(c_int(), c_int(), c_bool())

		self.myDll.loadProc("motion_isMoving")
		self.myDll.motion_isMoving.restype(c_bool())
		self.myDll.motion_isMoving.argtypes(c_int(), c_int())

		self.myDll.loadProc("_getCommand")
		self.myDll._getCommand.restype(c_double())
		self.myDll._getCommand.argtypes(c_int(), c_int())

		self.myDll.loadProc("_getActual")
		self.myDll._getActual.restype(c_double())
		self.myDll._getActual.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_stop")
		self.myDll.motion_stop.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_abort")
		self.myDll.motion_abort.argtypes(c_int(), c_int())

		self.myDll.loadProc("_ampFault")
		self.myDll._ampFault.restype(c_bool())
		self.myDll._ampFault.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_release_cmd")
		self.myDll.motion_release_cmd.argtypes(c_int(), c_int(), c_int())

		self.myDll.loadProc("motion_setPosition")
		self.myDll.motion_setPosition.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setAccel")
		self.myDll.motion_setAccel.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setDecel")
		self.myDll.motion_setDecel.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setJerk")
		self.myDll.motion_setJerk.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_setVelocity")
		self.myDll.motion_setVelocity.argtypes(c_int(), c_int(), c_double())

		self.myDll.loadProc("motion_clear")
		self.myDll.motion_clear.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_getLimitNStatus")
		self.myDll.motion_getLimitNStatus.restype(c_bool())
		self.myDll.motion_getLimitNStatus.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_getLimitPStatus")
		self.myDll.motion_getLimitPStatus.restype(c_bool())
		self.myDll.motion_getLimitPStatus.argtypes(c_int(), c_int())

		self.myDll.loadProc("motion_getHomeStatus")
		self.myDll.motion_getHomeStatus.restype(c_bool())
		self.myDll.motion_getHomeStatus.argtypes(c_int(), c_int())

		self.myDll.loadProc("_ClearSuperviser")
		self.myDll._ClearSuperviser.restype(c_int())
		self.myDll._ClearSuperviser.argtypes(c_int(), c_int(), c_int(), c_int())

		self.myDll.loadProc("_find_z_phase1")
		self.myDll._find_z_phase1.restype(c_int())
		self.myDll._find_z_phase1.argtypes(c_int(), c_int(), c_int(), c_double(), c_double(), c_double(), c_double())

		self.myDll.loadProc("_find_z_phase2")
		self.myDll._find_z_phase2.restype(c_int())
		self.myDll._find_z_phase2.argtypes(c_int(), c_int(), c_int(), c_double(), c_double(), c_double(), c_double())

		self.myDll.loadProc("_find_z_phase3")
		self.myDll._find_z_phase3.restype(c_int())
		self.myDll._find_z_phase3.argtypes(c_int(), c_int(), c_int(), c_double(), c_double(), c_double(), c_double())

		self.myDll.loadProc("_find_z_phase4")
		self.myDll._find_z_phase4.restype(c_int())
		self.myDll._find_z_phase4.argtypes(c_int(), c_int(), c_int(), c_double(), c_double(), c_double(), c_double())

		self.myDll.loadProc("_init_moveSeq")
		self.myDll._init_moveSeq.restype(c_int())
		self.myDll._init_moveSeq.argtypes(c_int(), c_int(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double())

		self.myDll.loadProc("_init_moveSeq_Touch")
		self.myDll._init_moveSeq_Touch.restype(c_int())
		self.myDll._init_moveSeq_Touch.argtypes(c_int(), c_int(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double(), c_double(), c_int(), c_double(), c_bool())
				
		self.myDll.loadProc("_autolevel_spdmode")
		self.myDll._autolevel_spdmode.restype(c_int())
		self.myDll._autolevel_spdmode.argtypes(c_int(), c_int(), c_double(), c_double(), c_double(), c_int(), c_double(), c_bool())

		self.myDll.loadProc("_SequenceStop")
		self.myDll._SequenceStop.restype(c_bool())
		self.myDll._SequenceStop.argtypes(c_int(), c_int())

		self.myDll.loadProc("_panic")
		self.myDll._panic.restype(c_bool())

		self.id = self.myDll.motion_open.call(index)
		self.ctrlIO = self.myDll
		self.ctrlIO.loadProc("_io_input")
		self.ctrlIO._io_input.restype(c_int())
		self.ctrlIO._io_input.argtypes(c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_getoutput")
		self.ctrlIO._io_getoutput.restype(c_int())
		self.ctrlIO._io_getoutput.argtypes(c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_getoutput_mt")
		self.ctrlIO._io_getoutput_mt.restype(c_int())
		self.ctrlIO._io_getoutput_mt.argtypes(c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_output_mt")
		self.ctrlIO._io_output_mt.restype(c_bool())
		self.ctrlIO._io_output_mt.argtypes(c_int(), c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_output")
		self.ctrlIO._io_output.restype(c_bool())
		self.ctrlIO._io_output.argtypes(c_int(), c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_output_analog")
		self.ctrlIO._io_output_analog.restype(c_bool())
		self.ctrlIO._io_output_analog.argtypes(c_int(), c_int(), c_int(), c_int(), c_int())

		self.ctrlIO.loadProc("_io_input_analog")
		self.ctrlIO._io_input_analog.restype(c_int())
		self.ctrlIO._io_input_analog.argtypes(c_int(), c_int(), c_int(), c_int())

	}
    
	def getDigital(self, idx: int) -> float
	{
		idx = idx + int(self.id) * 1000000
		res = self.ctrlIO._io_input.call(idx / 1000000, (idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100)
		if(res == 1)
		{
			return true
		}
		else
		{
			return false
		}
	}

    def setDigital(self, idx: int, bVal: bool)
	{
		idx = idx + int(self.id) * 1000000
		val = -1
		if(bVal)
		{
			val = 1
		}
		else
		{
			val = 0
		}
		if (9 == idx / 1000000)
		{
			self.ctrlIO._io_output_mt.call((idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100, val)
		}
		else
		{
			self.ctrlIO._io_output.call(idx / 1000000, (idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100, val)
		}
	}

    def getDigitalInternal(self, idx: int) -> float
	{
		idx = idx + int(self.id) * 1000000
		res = 0;
		if (9 == idx / 1000000) // motor io
		{
			res = self.ctrlIO._io_getoutput_mt.call((idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100)
		}
		else
		{
			res = self.ctrlIO._io_getoutput.call(idx / 1000000, (idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100);
		}
		if(res == 1)
		{
			return true
		}
		else
		{
			return false
		}
	}

	def getInputAnalog(self, idx:int)
	{
		idx = idx + int(self.id) * 1000000
		res = self.ctrlIO._io_input_analog.call(idx / 1000000, (idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100)
		return res
	}

	def setOutputAnalog(self, idx : int, val:int)
	{
		idx = idx + int(self.id) * 1000000
		self.ctrlIO._io_output_analog.call(idx / 1000000, (idx % 1000000) / 10000, (idx % 10000) / 100, idx % 100, val);
	}

	def terminate(self)
	{
		self.myDll.motion_close.call(self.id)
	}

	def initMotor(self, axis: int, nOption: int)
	{
		self.myDll._initMotor.call(self.id, axis, nOption)
	}

	def isAlarm(self, axis: int)
	{
		return self.myDll.motion_isAlarm.call(self.id, axis)
	}

	def enable(self, axis: int, enable: bool)
	{
		self.myDll.motion_enable.call(self.id, axis, enable)
	}

	def isEnabled(self, axis: int)
	{
		return self.myDll.motion_isEnabled.call(self.id, axis)
	}

	def moveSync(self, axis: int, pos: float)
	{
		self.myDll.motion_move.call(self.id, axis, pos)
		self.wait(axis)
	}

	def relMove(self, axis: int, pos: float)
	{
		self.myDll.motion_relMove.call(self.id, axis, pos)
	}

	def velMove(self, axis: int, reverse: bool)
	{
		self.myDll.motion_velMove.call(self.id, axis, reverse)
	}

	def move(self, axis: int, pos: float)
	{
		self.myDll.motion_move.call(self.id, axis, pos)
	}

	def relMoveSync(self, axis: int, pos: float)
	{
		self.myDll.motion_relMove.call(self.id, axis, pos)
		self.wait(axis)
	}

	def isMoving(self, axis: int)
	{
		return self.myDll.motion_isMoving.call(self.id, axis)
	}

	def getCmdPos(self, axis: int)
	{
		dblCmdPos = self.myDll._getCommand.call(self.id, axis)
		return dblCmdPos
	}

	def getActPos(self, axis: int)
	{
		return self.myDll._getActual.call(self.id, axis)
	}

	def stop(self, axis: int)
	{
		self.myDll.motion_stop.call(self.id, axis)
	}

	def abort(self, axis: int)
	{
		self.myDll.motion_abort.call(self.id, axis)
	}

	def ampFault(self, axis: int)
	{
		return self.myDll._ampFault.call(self.id, axis)
	}

	def release_cmd(self, axis: int)
	{
		self.myDll.motion_release_cmd.call(self.id, axis)
	}

	def setPosition(self, axis: int, pos: float)
	{
		self.myDll.motion_setPosition.call(self.id, axis, pos)
	}

	def setAccel(self, axis: int, value: float)
	{
		self.myDll.motion_setAccel.call(self.id, axis, value)
	}

	def setDecel(self, axis: int, value: float)
	{
		self.myDll.motion_setDecel.call(self.id, axis, value)
	}

	def setJerk(self, axis: int, value: float)
	{
		self.myDll.motion_setJerk.call(self.id, axis, value)
	}

	def setVelocity(self, axis: int, value: float)
	{
		self.myDll.motion_setVelocity.call(self.id, axis, value)
	}

	def clear(self, axis: int)
	{
		self.myDll.motion_clear.call(self.id, axis)
	}

	def getLimitNStatus(self, axis: int)
	{
		return self.myDll.motion_getLimitNStatus.call(self.id, axis)
	}

	def getLimitPStatus(self, axis: int)
	{
		return self.myDll.motion_getLimitPStatus.call(self.id, axis)
	}

	def getHomeStatus(self, axis: int)
	{
		return self.myDll.motion_getHomeStatus.call(self.id, axis)
	}

	def ClearSuperviser(self, axis1: int, axis2: int, union_axis: int)
	{
		return self.myDll._ClearSuperviser.call(self.id, axis1, axis2, union_axis)
	}

	def find_z_phase1(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		return self.myDll._find_z_phase1.call(mode, self.id, axis, pls_rev, vel, acc, jerk)
	}

	def find_z_phase2(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		return self.myDll._find_z_phase2.call(mode, self.id, axis, pls_rev, vel, acc, jerk)
	}

	def find_z_phase3(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		return self.myDll._find_z_phase3.call(mode, self.id, axis, pls_rev, vel, acc, jerk)
	}

	def find_z_phase4(self, mode: int, axis: int, pls_rev: float, vel: float, acc: float, jerk: float)
	{
		return self.myDll._find_z_phase4.call(mode, self.id, axis, pls_rev, vel, acc, jerk)
	}

	def moveSeq(self, axis: int, pos1: float, vel1: float, acc1: float, jerk1: float, pos2: float, vel2: float, acc2: float, jerk2: float)
	{
		return self.myDll._init_moveSeq.call(axis, pos1, vel1, acc1, jerk1, pos2, vel2, acc2, jerk2)
	}

	def moveSeq_Touch(self, axis1: int, pos1: float, vel1: float, acc1: float, jerk1: float, pos2: float, vel2: float, acc2: float, jerk2: float, axis_enc: int, encoder_targer: float, bUseGaninTable: bool)
	{
		return self.myDll._init_moveSeq_Touch.call(axis1, pos1, vel1, acc1, jerk1, pos2, vel2, acc2, jerk2, axis_enc, encoder_targer, bUseGaninTable)
	}
	
	def AutoLevel_SpdMode(self, axis: int, vel: float, acc: float, jerk: float, axis_enc: int, encoder_targer: float, bUseGaninTable: bool)
	{
		return self.myDll._autolevel_spdmode.call(self.id, axis, vel, acc, jerk, axis_enc, encoder_targer, bUseGaninTable)
	}

	def _SequenceStop(self, axis: int)
	{
		return self.myDll._SequenceStop.call(self.id, axis)
	}

	def panic(self)
	{
		self.myDll._panic.call()
	}
}

class VirtualIOController(AbstractIOController)
{
	def __init__(self, name: str)
	{
		AbstractIOController.__init__(self, name)
		self.initialize(name)
	}

	def initialize(self, name: str)
	{
		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\VirtualDriver_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\VirtualDriver_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\VirtualDriver_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Release\\VirtualDriver_32.dll")
			}
		}

		self.myDll.loadProc("io_open")
		self.myDll.io_open.restype(c_int())
		self.myDll.io_open.argtypes(c_string())

		self.myDll.loadProc("io_getDIValue")
		self.myDll.io_getDIValue.restype(c_bool())
		self.myDll.io_getDIValue.argtypes(c_int(), c_int())

		self.myDll.loadProc("io_setDOValue")
		self.myDll.io_setDOValue.argtypes(c_int(), c_int(), c_bool())

		self.myDll.loadProc("io_getAIValue")
		self.myDll.io_getAIValue.restype(c_double())
		self.myDll.io_getAIValue.argtypes(c_int(), c_int())

		self.myDll.loadProc("io_setAOValue")
		self.myDll.io_setAOValue.argtypes(c_int(), c_int(), c_double())

		self.id = self.myDll.io_open.call(name)

		self.dictInternalDOValue = dict()
		self.dictInternalAOValue = dict()
	}

	def terminate(self)
	{
	}

	def getDigital(self, idx: int)
	{
        print("-------------GETDIGITAL------------")
		return self.myDll.io_getDIValue.call(self.id, idx)
	}

	def setDigital(self, index: int, value: bool)
	{
		self.myDll.io_setDOValue.call(self.id, index, value)

		self.dictInternalDOValue.setModify(index, value)
	}

	def getDigitalInternal(self, index: int)
	{
		value = false

		if(self.dictInternalDOValue.contains(index))
		{
			value = self.dictInternalDOValue.get(index)
		}

		return value
	}

	def getAnalog(self, index: int)
	{
		return self.myDll.io_getAIValue.call(self.id, index)
	}

	def setAnalog(self, index: int, value: float)
	{
		self.myDll.io_setAOValue.call(self.id, index, value)

		self.dictInternalAOValue.setModify(index, value)
	}

	def getAnalogInternal(self, index: int)
	{
		value = 0.0

		if(self.dictInternalAOValue.contains(index))
		{
			value = self.dictInternalAOValue.get(index)
		}

		return value
	}
}

class SecsgemController(AbstractController)
{
	class XGEMState()
	{
		Init = 0
		Idle = 1
		Setup = 2
		Ready = 3
		Execute = 4
	}

	class CommunicationState()
	{
		NoneState = -1
		CommDisabled = 1
		WaitCRFromHost = 2
		WaitDelay = 3
		WaitCRA = 4
		Communicating = 5
	}

	class ControlState()
	{
		NoneState = -1
		EquipmentOffLine = 1
		AttemptOnLine = 2
		HostOffLine = 3
		Local = 4
		Remote = 5
	}

	class PPGNTAck()
	{
		OK = 0
		Alreadyhave = 1
		NoSpace = 2
		InvalidPPID = 3
		Busy = 4
		WillNotAccept = 5

		//>5 = Other error
	}

	class ACKC7Ack()
	{
		Accepted = 0
		PermissionNotGranted = 1
		LengthError = 2
		MatrixOverflow = 3
		PPIDNotFound = 4
		ModeUnsupported = 5
		CommandWillBePerformed = 6
		//>6 = Other error
	}

	class Verification()
	{
		NoError = 0
		//<0 : Error
	}

	class SpoolState()
	{
		INACTIVE = 0
		ACTIVE = 1
	}

	class SpoolLoadState()
	{
		LDNOTFULL = 0
		LDFULL = 1
	}

	class SpoolUnloadState()
	{
		NOOUTPUT = 0
		TRANSMIT = 1
		PURGE = 2
	}

	def __init__(self, name: str)
	{
		AbstractController.__init__(self, name)

		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\SecsgemDriver_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\SecsgemDriver_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\SecsgemDriver_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Release\\SecsgemDriver_32.dll")
			}
		}

		self.myDll.loadProc("__initialize")
		self.myDll.__initialize.restype(c_int())
		self.myDll.__initialize.argtypes(c_string())

		self.myDll.loadProc("__start")
		self.myDll.__start.restype(c_int())

		self.myDll.loadProc("__stop")
		self.myDll.__stop.restype(c_int())

		self.myDll.loadProc("__close")
		self.myDll.__close.restype(c_int())

		self.myDll.loadProc("GEMReqOffline")
		self.myDll.GEMReqOffline.restype(c_int())

		self.myDll.loadProc("GEMReqLocal")
		self.myDll.GEMReqLocal.restype(c_int())

		self.myDll.loadProc("GEMReqRemote")
		self.myDll.GEMReqRemote.restype(c_int())

		self.myDll.loadProc("GEMReqHostOffline")
		self.myDll.GEMReqHostOffline.restype(c_int())

		self.myDll.loadProc("GEMSetEstablish")
		self.myDll.GEMSetEstablish.restype(c_int())
		self.myDll.GEMSetEstablish.argtypes(c_int())

		self.myDll.loadProc("GEMEQInitialized")
		self.myDll.GEMEQInitialized.restype(c_int())
		self.myDll.GEMEQInitialized.argtypes(c_int())

		self.myDll.loadProc("GEMSetVariable")
		self.myDll.GEMSetVariable.restype(c_int())
		self.myDll.GEMSetVariable.argtypes(c_int(), c_string())

		self.myDll.loadProc("GEMGetVariable")
		self.myDll.GEMGetVariable.restype(c_int())
		self.myDll.GEMGetVariable.argtypes(c_int(), c_pointer(c_string()))

		self.myDll.loadProc("MakeObject")
		self.myDll.MakeObject.restype(c_int())
		self.myDll.MakeObject.argtypes(c_pointer(c_long()))

		self.myDll.loadProc("SetList")
		self.myDll.SetList.restype(c_long())
		self.myDll.SetList.argtypes(c_long(), c_long())

		self.myDll.loadProc("GetList")
		self.myDll.GetList.restype(c_long())
		self.myDll.GetList.argtypes(c_long(), c_pointer(c_long()))

		self.myDll.loadProc("SetBinary")
		self.myDll.SetBinary.restype(c_long())
		self.myDll.SetBinary.argtypes(c_long(), c_pointer(c_short()), c_long())

		self.myDll.loadProc("SetBool")
		self.myDll.SetBool.restype(c_long())
		self.myDll.SetBool.argtypes(c_long(), c_pointer(c_short()), c_long())

		self.myDll.loadProc("SetU1")
		self.myDll.SetU1.restype(c_long())
		self.myDll.SetU1.argtypes(c_long(), c_pointer(c_short()), c_long())

		self.myDll.loadProc("SetU2")
		self.myDll.SetU2.restype(c_long())
		self.myDll.SetU2.argtypes(c_long(), c_pointer(c_long()), c_long())

		self.myDll.loadProc("SetU4")
		self.myDll.SetU4.restype(c_long())
		self.myDll.SetU4.argtypes(c_long(), c_pointer(c_double()), c_long())

		self.myDll.loadProc("SetU8")
		self.myDll.SetU8.restype(c_long())
		self.myDll.SetU8.argtypes(c_long(), c_pointer(c_double()), c_long())

		self.myDll.loadProc("SetI1")
		self.myDll.SetI1.restype(c_long())
		self.myDll.SetI1.argtypes(c_long(), c_pointer(c_short()), c_long())

		self.myDll.loadProc("SetI2")
		self.myDll.SetI2.restype(c_long())
		self.myDll.SetI2.argtypes(c_long(), c_pointer(c_short()), c_long())

		self.myDll.loadProc("SetI4")
		self.myDll.SetI4.restype(c_long())
		self.myDll.SetI4.argtypes(c_long(), c_pointer(c_long()), c_long())

		self.myDll.loadProc("SetI8")
		self.myDll.SetI8.restype(c_long())
		self.myDll.SetI8.argtypes(c_long(), c_pointer(c_long()), c_long())

		self.myDll.loadProc("SetF4")
		self.myDll.SetF4.restype(c_long())
		self.myDll.SetF4.argtypes(c_long(), c_pointer(c_float()), c_long())

		self.myDll.loadProc("SetF8")
		self.myDll.SetF8.restype(c_long())
		self.myDll.SetF8.argtypes(c_long(), c_pointer(c_double()), c_long())

		self.myDll.loadProc("SetAscii")
		self.myDll.SetAscii.restype(c_long())
		self.myDll.SetAscii.argtypes(c_long(), c_pointer(c_char()), c_long())

		self.myDll.loadProc("GetBinary")
		self.myDll.GetBinary.restype(c_long())
		self.myDll.GetBinary.argtypes(c_long(), c_pointer(c_short()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetBool")
		self.myDll.GetBool.restype(c_long())
		self.myDll.GetBool.argtypes(c_long(), c_pointer(c_short()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetU1")
		self.myDll.GetU1.restype(c_long())
		self.myDll.GetU1.argtypes(c_long(), c_pointer(c_short()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetU2")
		self.myDll.GetU2.restype(c_long())
		self.myDll.GetU2.argtypes(c_long(), c_pointer(c_long()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetU4")
		self.myDll.GetU4.restype(c_long())
		self.myDll.GetU4.argtypes(c_long(), c_pointer(c_double()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetU8")
		self.myDll.GetU8.restype(c_long())
		self.myDll.GetU8.argtypes(c_long(), c_pointer(c_double()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetI1")
		self.myDll.GetI1.restype(c_long())
		self.myDll.GetI1.argtypes(c_long(), c_pointer(c_short()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetI2")
		self.myDll.GetI2.restype(c_long())
		self.myDll.GetI2.argtypes(c_long(), c_pointer(c_short()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetI4")
		self.myDll.GetI4.restype(c_long())
		self.myDll.GetI4.argtypes(c_long(), c_pointer(c_long()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetI8")
		self.myDll.GetI8.restype(c_long())
		self.myDll.GetI8.argtypes(c_long(), c_pointer(c_long()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetF4")
		self.myDll.GetF4.restype(c_long())
		self.myDll.GetF4.argtypes(c_long(), c_pointer(c_float()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetF8")
		self.myDll.GetF8.restype(c_long())
		self.myDll.GetF8.argtypes(c_long(), c_pointer(c_double()), c_pointer(c_long()), c_long())

		self.myDll.loadProc("GetAscii")
		self.myDll.GetAscii.restype(c_long())
		self.myDll.GetAscii.argtypes(c_long(), c_pointer(c_char()), c_pointer(c_long()), c_long())

		self.myDll.registerCallbackFunc("XGEMStateEvent", self.onXGEMStateEvent, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMCommStateChanged", self.onGEMCommStateChanged, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMControlStateChanged", self.onGEMControlStateChanged, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMErrorEvent", self.onGEMErrorEvent, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMRspAllECInfo", self.onGEMRspAllECInfo, (c_void(), c_long(), c_pointer(c_long()), c_pointer(c_string()), c_pointer(c_string()), c_pointer(c_string()), c_pointer(c_string()), c_pointer(c_string()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMReqDateTime", self.onGEMReqDateTime, (c_void(), c_long(), c_string()))
		self.myDll.registerCallbackFunc("GEMECVChanged", self.onGEMECVChanged, (c_void(), c_long(), c_pointer(c_long()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMReqChangeECV", self.onGEMReqChangeECV, (c_void(), c_long(), c_long(), c_pointer(c_long()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMTerminalMessage", self.onGEMTerminalMessage, (c_void(), c_long(), c_string()))
		self.myDll.registerCallbackFunc("GEMTerminalMultiMessage", self.onGEMTerminalMultiMessage, (c_void(), c_long(), c_long(), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMReqGetDateTime", self.onGEMReqGetDateTime, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMRspGetDateTime", self.onGEMRspGetDateTime, (c_void(), c_string()))
		self.myDll.registerCallbackFunc("GEMRspPPLoadInquire", self.onGEMRspPPLoadInquire, (c_void(), c_string(), c_long()))
		self.myDll.registerCallbackFunc("GEMRspPPSend", self.onGEMRspPPSend, (c_void(), c_string(), c_long()))
		self.myDll.registerCallbackFunc("GEMRspPP", self.onGEMRspPP, c_void(), (c_string(), c_string()))
		self.myDll.registerCallbackFunc("GEMRspPPFmtSend", self.onGEMRspPPFmtSend, (c_void(), c_string(), c_long()))
		self.myDll.registerCallbackFunc("GEMRspPPFmt", self.onGEMRspPPFmt, c_void(), (c_string(), c_string(), c_string(), c_long(), c_pointer(c_string()), c_pointer(c_long()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMRspPPFmtVerification", self.onGEMRspPPFmtVerification, (c_void(), c_string(), c_long()))
		self.myDll.registerCallbackFunc("GEMReqPPLoadInquire", self.onGEMReqPPLoadInquire, (c_void(), c_long(), c_string(), c_long()))
		self.myDll.registerCallbackFunc("GEMReqPPSend", self.onGEMReqPPSend, (c_void(), c_long(), c_string(), c_string()))
		self.myDll.registerCallbackFunc("GEMReqPP", self.onGEMReqPP, c_void(), (c_long(), c_string()))
		self.myDll.registerCallbackFunc("GEMReqPPDelete", self.onGEMReqPPDelete, (c_void(), c_long(), c_long(), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMReqPPList", self.onGEMReqPPList, (c_void(), c_long()))
		self.myDll.registerCallbackFunc("GEMReqPPFmtSend", self.onGEMReqPPFmtSend, (c_void(), c_long(), c_string(), c_string(), c_string(), c_long(), c_pointer(c_string()), c_pointer(c_long()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("GEMReqPPFmt", self.onGEMReqPPFmt, (c_void(), c_long(), c_string()))
		self.myDll.registerCallbackFunc("GEMReqRemoteCommand", self.onGEMReqRemoteCommand, (c_void(), c_long(), c_string(), c_long(), c_pointer(c_string()), c_pointer(c_string())))
		self.myDll.registerCallbackFunc("SECSMessageReceived", self.onSECSMessageReceived, (c_void(), c_long(), c_long(), c_long(), c_long()))
		self.myDll.registerCallbackFunc("GEMSpoolStateChanged", self.onGEMSpoolStateChanged, (c_void(), c_long(), c_long(), c_long(), c_string(), c_long(), c_long(), c_long(), c_long()))
	}

	def onXGEMStateEvent(self, state: int)
	{
		if (state == SecsgemController.XGEMState.Execute)
		{
			self.GEMSetEstablish(1);
			self.GEMEQInitialized(1);
		}
	}

	def onGEMCommStateChanged(self, state: int)
	{
	}

	def	onGEMControlStateChanged(self, state: int)
	{
	}

	def onGEMErrorEvent(self, errorCode: int)
	{
	}

	def onGEMRspAllECInfo(self, count: int, vid: array, name: array, value: array, default: array, min: array, max: array, unit: array)
	{
	}

	def	onGEMReqDateTime(self, msgID: int, time: str)
	{
	}

	def	onGEMECVChanged(self, count: int, ecid: array, value: array)
	{
	}

	def	onGEMReqChangeECV(self, msgID: int, count: int, ecid: array, value: array)
	{
	}

	def	onGEMTerminalMessage(self, tid: int, msg: str)
	{
	}

	def	onGEMTerminalMultiMessage(self, tid: int, count: int, msg: array)
	{
	}

	def	onGEMReqGetDateTime(self, msgID: int)
	{
	}

	def	onGEMRspGetDateTime(self, time: str)
	{
	}

	def	onGEMRspPPLoadInquire(self, ppid: str, result: int)
	{
	}

	def	onGEMRspPPSend(self, ppid: str, result: int)
	{
	}

	def	onGEMRspPP(self, ppid: str, body: str)
	{
	}

	def	onGEMRspPPFmtSend(self, ppid: str, result: int)
	{
	}

	def	onGEMRspPPFmt(self, ppid: str, mdln: str, softRev: str, count: int, ccode: array, paramCount: array, paramName: array)
	{
	}

	def onGEMRspPPFmtVerification(self, ppid: str, result: int)
	{
	}

	def	onGEMReqPPLoadInquire(self, msgID: int, ppid: str, length: int)
	{
	}

	def onGEMReqPPSend(self, msgID: int, ppid: str, body: str)
	{
	}

	def	onGEMReqPP(self, msgID: int, ppid: str)
	{
	}

	def	onGEMReqPPDelete(self, msgID: int, count: int, ppid: array)
	{
	}

	def	onGEMReqPPList(self, msgID: int)
	{
	}

	def	onGEMReqPPFmtSend(self, msgID: int, ppid: str, mdln: str, softRev: str, count: int, ccode: array, paramCount: array, paramName: array)
	{
	}

	def	onGEMReqPPFmt(self, msgID: int, ppid: str)
	{
	}

	def	onGEMReqRemoteCommand(self, msgID: int, rcmd: str, count: int, name: array, value: array)
	{
	}

	def	onSECSMessageReceived(self, objectID: int, stream: int, function: int, sysbyte: int)
	{
	}

	def	onGEMSpoolStateChanged(self, state: int, loadState: int, unloadState: int, fullTime: str, maxTransmit: int, msgNum: int, totalNum: int, transmitFail: int)
	{
	}


	def initialize(self, cfg: str)
	{
		return self.myDll.__initialize.call(cfg)
	}

	def start(self)
	{
		return self.myDll.__start.call()
	}

	def stop(self)
	{
		return self.myDll.__stop.call()
	}

	def close(self)
	{
		return self.myDll.__close.call()
	}

	def GEMReqOffline(self)
	{
		return self.myDll.GEMReqOffline.call()
	}

	def GEMReqLocal(self)
	{
		return self.myDll.GEMReqLocal.call()
	}

	def GEMReqRemote(self)
	{
		return self.myDll.GEMReqRemote.call()
	}

	def GEMReqHostOffline(self)
	{
		return self.myDll.GEMReqHostOffline.call()
	}

	def GEMSetEstablish(self, state: int)
	{
		return self.myDll.GEMSetEstablish.call(state)
	}

	def GEMEQInitialized(self, initType: int)
	{
		return self.myDll.GEMEQInitialized.call(initType)
	}

	def GEMSetVariable(self, vid: int, value: str)
	{
		return self.myDll.GEMSetVariable.call(vid, value)
	}

	def GEMGetVariable(self, vid: int, value: str)
	{
		return self.myDll.GEMGetVariable.call(vid, value)
	}

	def MakeObject(self, objectID: int)
	{
		return self.myDll.MakeObject.call(objectID)
	}

	def SetList(self, objectID: int, itemCount: int)
	{
		return self.myDll.SetList.call(objectID, itemCount)
	}

	def GetList(self, objectID: int, itemCount: int)
	{
		return self.myDll.GetList.call(objectID, itemCount)
	}

	def SetBinary(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetBinary.call(objectID, listValue, itemCount)
	}

	def SetBool(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetBool.call(objectID, listValue, itemCount)
	}

	def SetU1(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetU1.call(objectID, listValue, itemCount)
	}

	def SetU2(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetU2.call(objectID, listValue, itemCount)
	}

	def SetU4(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetU4.call(objectID, listValue, itemCount)
	}

	def SetU8(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetU8.call(objectID, listValue, itemCount)
	}

	def SetI1(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetI1.call(objectID, listValue, itemCount)
	}

	def SetI2(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetI2.call(objectID, listValue, itemCount)
	}

	def SetI4(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetI4.call(objectID, listValue, itemCount)
	}

	def SetI8(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetI8.call(objectID, listValue, itemCount)
	}

	def SetF4(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetF4.call(objectID, listValue, itemCount)
	}

	def SetF8(self, objectID: int, listValue: array, itemCount: int)
	{
		return self.myDll.SetF8.call(objectID, listValue, itemCount)
	}

	def SetAscii(self, objectID: int, strValue: str, itemCount: int)
	{
		return self.myDll.SetAscii.call(objectID, strValue, itemCount)
	}

	def GetBinary(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetBinary.call(objectID, listValue, itemCount, size)
	}

	def GetBool(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetBool.call(objectID, listValue, itemCount, size)
	}

	def GetU1(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetU1.call(objectID, listValue, itemCount, size)
	}

	def GetU2(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetU2.call(objectID, listValue, itemCount, size)
	}

	def GetU4(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetU4.call(objectID, listValue, itemCount, size)
	}

	def GetU8(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetU8.call(objectID, listValue, itemCount, size)
	}

	def GetI1(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetI1.call(objectID, listValue, itemCount, size)
	}

	def GetI2(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetI2.call(objectID, listValue, itemCount, size)
	}

	def GetI4(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetI4.call(objectID, listValue, itemCount, size)
	}

	def GetI8(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetI8.call(objectID, listValue, itemCount, size)
	}

	def GetF4(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetF4.call(objectID, listValue, itemCount, size)
	}

	def GetF8(self, objectID: int, listValue: array, itemCount: int, size: int)
	{
		return self.myDll.GetF8.call(objectID, listValue, itemCount, size)
	}

	def GetAscii(self, objectID: int, strValue: str, itemCount: int, size: int)
	{
		return self.myDll.GetAscii.call(objectID, strValue, itemCount, size)
	}
}

class ImageViewerTest()
{
	def __init__(self)
	{
		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\ImageViewerDll_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\ImageViewerDll_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\ImageViewerDll_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Release\\ImageViewerDll_32.dll")
			}
		}

		self.myDll.loadProc("_register")
		self.myDll._register.argtypes(c_long())
		
#		self.myDll.loadProc("tBool")
#		self.myDll.tBool.argtypes(c_bool())
		
#		self.myDll.loadProc("tShort")
#		self.myDll.tShort.argtypes(c_short())
		
#		self.myDll.loadProc("tInt")
#		self.myDll.tInt.argtypes(c_int())
		
#		self.myDll.loadProc("tFloat")
#		self.myDll.tFloat.argtypes(c_float())
		
#		self.myDll.loadProc("tDouble")
#		self.myDll.tDouble.argtypes(c_double())
		
#		self.myDll.loadProc("tIntA")
#		self.myDll.tIntA.argtypes(c_array(c_int(), 10))
		
#		self.myDll.loadProc("tIntAA")
#		self.myDll.tIntAA.restype(c_array(c_array(c_int(), 5), 5))
#		self.myDll.tIntAA.argtypes(c_array(c_array(c_int(), 5), 10))
		
#		self.myDll.loadProc("tDoubleAA")
#		self.myDll.tDoubleAA.restype(c_array(c_array(c_double(), 5), 10))
#		self.myDll.tDoubleAA.argtypes(c_array(c_array(c_double(), 5), 10))
		
#		self.myDll.loadProc("tDoubleP")
#		self.myDll.tDoubleP.restype(c_pointer(c_double()))
#		self.myDll.tDoubleP.argtypes(c_pointer(c_double()), c_int())
		
#		self.myDll.loadProc("tString")
#		self.myDll.tString.restype(c_string())
#		self.myDll.tString.argtypes(c_string())
		
#		self.myDll.loadProc("tStringA")
#		self.myDll.tStringA.restype(c_string())
#		self.myDll.tStringA.argtypes(c_pointer(c_string()))
		
#		self.myDll.loadProc("tDoublePO")
#		self.myDll.tDoublePO.restype(c_pointer(c_double()))
		
#		self.myDll.loadProc("tDoublePPO")
#		self.myDll.tDoublePPO.restype(c_pointer(c_pointer(c_double())))
		
#		self.myDll.loadProc("tDoublePP")
#		self.myDll.tDoublePP.argtypes(c_pointer(c_pointer(c_double())))
#		self.myDll.tDoublePP.restype(c_pointer(c_double()))
		
#		self.myDll._register.call(obj)
	}
}

class DispenserVision()
{
	def __init__(self)
	{
		if(isBuild64bit())
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Debug\\DispenserVisionDll_64_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\x64_Release\\DispenserVisionDll_64.dll")
			}
		}
		else
		{
			if(isBuildDebug())
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Debug\\DispenserVisionDll_32_d.dll")
			}
			else
			{
				self.myDll = ctypes_cdll("..\\..\\Libs\\Win32_Release\\DispenserVisionDll_32.dll")
			}
		}

		self.myDll.loadProc("setHandle")
		self.myDll.setHandle.argtypes(c_int())
		
		self.myDll.loadProc("getHandle")
		self.myDll.getHandle.restype(c_int())
		
		self.myDll.loadProc("setChannelCount")
		self.myDll.setChannelCount.argtypes(c_int())
		
		self.myDll.loadProc("selectChannel")
		self.myDll.selectChannel.argtypes(c_int())
		
		self.myDll.loadProc("selectAlign")
		self.myDll.selectAlign.argtypes(c_int())
		
		self.myDll.loadProc("selectBlob")
		self.myDll.selectBlob.argtypes(c_int())
		
		self.myDll.loadProc("openImage")
		
		self.myDll.loadProc("runAlign")
		self.myDll.runAlign.argtypes(c_int())
		
		self.myDll.loadProc("runBlob")
		self.myDll.runBlob.argtypes(c_int())
		
		self.myDll.loadProc("load")
		
		self.myDll.loadProc("save")
		
		self.myDll.loadProc("getSelectedChannel")
		self.myDll.getSelectedChannel.restype(c_int())
		
		self.myDll.loadProc("getSelectedAlign")
		self.myDll.getSelectedAlign.restype(c_int())
		
		self.myDll.loadProc("getSelectedBlob")
		self.myDll.getSelectedBlob.restype(c_int())
		
		self.myDll.loadProc("isEditTrain")
		self.myDll.isEditTrain.restype(c_bool())
		
		self.myDll.loadProc("editTrain")
		
		self.myDll.loadProc("applyTrain")
		
		self.myDll.loadProc("cancelTrain")
		
		self.myDll.loadProc("setEditorMode")
		
		self.myDll.loadProc("setViewerMode")
		
		self.myDll.loadProc("startLive")
		self.myDll.startLive.argtypes(c_int())
		
		self.myDll.loadProc("stopLive")
		self.myDll.stopLive.argtypes(c_int())
		
		self.myDll.loadProc("isLive")
		self.myDll.isLive.argtypes(c_int())
		self.myDll.isLive.restype(c_bool())
		
		self.myDll.loadProc("grab")
		self.myDll.grab.argtypes(c_int())
		
		self.myDll.loadProc("loadGlobalData")
		
		self.myDll.loadProc("saveGlobalData")
		
		self.myDll.loadProc("getAlignResultCount")
		self.myDll.getAlignResultCount.argtypes(c_int())
		self.myDll.getAlignResultCount.restype(c_int())
		
		self.myDll.loadProc("getAlignResultScore")
		self.myDll.getAlignResultScore.argtypes(c_int())
		self.myDll.getAlignResultScore.restype(c_pointer(c_double()))
		
		self.myDll.loadProc("getAlignResultX")
		self.myDll.getAlignResultX.argtypes(c_int())
		self.myDll.getAlignResultX.restype(c_pointer(c_double()))
		
		self.myDll.loadProc("getAlignResultY")
		self.myDll.getAlignResultY.argtypes(c_int())
		self.myDll.getAlignResultY.restype(c_pointer(c_double()))
		
		self.myDll.loadProc("getAlignResultTheta")
		self.myDll.getAlignResultTheta.argtypes(c_int())
		self.myDll.getAlignResultTheta.restype(c_pointer(c_double()))
		
		self.myDll.loadProc("getAlignResultRealX")
		self.myDll.getAlignResultRealX.argtypes(c_int())
		self.myDll.getAlignResultRealX.restype(c_pointer(c_double()))
		
		self.myDll.loadProc("getAlignResultRealY")
		self.myDll.getAlignResultRealY.argtypes(c_int())
		self.myDll.getAlignResultRealY.restype(c_pointer(c_double()))		
	}
}

class Property()
{
	def __init__(self)
	{
		
	}
}

class InheritedProperty(Property)
{
	class Data()
	{
		def __init__(self)
		{
			self.item = ""
			self.value = 0
		}
	}
	
	class Parameter()
	{
		def __init__(self)
		{
			self.name = ""
			self.listData = list()
		}
		
		def getValue(self, strItem : str)
		{
			value = None
			
			for i in range(self.listData.count())
			{
				data = self.listData.get(i)
				if(data.item == strItem)
				{
					value = data.value
					break
				}
			}
			
			return value
		}
	}
	
	def __init__(self)	
	{
		self.listInheritParameterItem = list()
		self.listRegisteredInheritParameter = list()
		
#		self.dictRegisteredInheritParameterGroup = dict()
	}
	
	def setInheritParameterItem(self, listItem : list)
	{
		self.listInheritParameterItem = listItem
	}
	
	def getParameter(self, strName : str)
	{
		paramReturn = InheritedProperty.Parameter()
	
		for i in range(self.listRegisteredInheritParameter.count())
		{
			param = self.listRegisteredInheritParameter.get(i)
			if(param.name == strName)
			{
				paramReturn = param
				break
			}
		}
	
		return paramReturn
	}
}

class DerivedProperty(Property)
{
	def __init__(self)
	{
		self.selectedParameterName = ""
		self.selectedParameter = None
	}
	
	def getParameterValue(self, strItem : str)
	{
		value = None
		
		if(hasattr(self, "selectedParameter"))
		{
			if(self.selectedParameter != None)
			{
				value = self.selectedParameter.getValue(strItem)
			}
		}
		
		return value
	}
}

class Atom()	
{
	def __init__(self)	
	{
		self.typeName = ""
		self.objectName = ""
		self.property = None
		self.uuid = uuid_gen()
		self.program = None
	}
}
class Attribute(Atom)	
{
	def __init__(self)	
	{
		Atom.__init__(self)
	}
}
class Command(Atom)	
{
	def __init__(self)	
	{
		Atom.__init__(self)
	}
	
	def execute(self, actor : Actor)
	{
	}
}
class AtomNode()	
{
	def __init__(self, atom : Atom)	
	{
		self.atom = atom
		self.listChildren = list()
	}
	
	def internal_GetDFS(self, atomNode : AtomNode, listDFS : list)
	{
		for i in range(atomNode.listChildren.count())
		{
			childAtomNode = atomNode.listChildren.get(i)
			if(childAtomNode != None)
			{
				if(childAtomNode.atom != None)
				{
					listDFS.append(childAtomNode)
				}
				
				self.internal_GetDFS(childAtomNode, listDFS)
			}
		}
	}
	
	def getDFS(self)
	{
		listDFS = list()
		
		self.internal_GetDFS(self, listDFS)
		
		return listDFS
	}
}
class AtomSet()	
{
	def __init__(self)	
	{
		self.rootAtomNode = AtomNode(None)
	}
	
	def getDFS(self)
	{
		listDFS = self.rootAtomNode.getDFS()
	
		return listDFS
	}
	
	def findAtomNode(self, objectName : str)
	{
		atomNodeReturn = None
		
		listDFS = self.getDFS()
		
		for i in range(listDFS.count())
		{
			atomNode = listDFS.get(i)
			
			if(atomNode.atom.objectName == objectName)
			{
				atomNodeReturn = atomNode
				break
			}
		}
		
		return atomNodeReturn
	}
	
	def internal_getParentAtom(self, atom : Atom, atomNode : AtomNode)
	{
		parentAtom = None
		
		for i in range(atomNode.listChildren.count())
		{
			childAtomNode = atomNode.listChildren.get(i)
			if(childAtomNode != None)
			{
				if(childAtomNode.atom == atom)
				{
					parentAtom = atomNode.atom
					break
				}
				
				parentAtom = self.internal_getParentAtom(atom, childAtomNode)
				if(parentAtom != None)
				{
					break
				}
			}
		}
		
		
		return parentAtom
	}
	
	def getParentAtom(self, atom : Atom)
	{
		parentAtom = self.internal_getParentAtom(atom, self.rootAtomNode)
	
		return parentAtom
	}
}
class Model(AtomSet)	
{
	def __init__(self)	
	{
		AtomSet.__init__(self)
	}
}
class Functions(AtomSet)	
{
	def __init__(self)	
	{
		AtomSet.__init__(self)
		
		self.atomNodeInstructionPointer = None
	}
	
	def loopWork(self, atomNode : AtomNode)
	{
		if(atomNode.atom != None)
		{
			self.atomNodeInstructionPointer = atomNode
			atomNode.atom.execute()
		}
		
		for i in range(atomNode.listChildren.count())
		{
			childAtomNode = atomNode.listChildren.get(i)
			
			self.loopWork(childAtomNode)
		}
	}
	
	def getSiblingAtomNode(self)
	{
		atomNodeReturn = None
		
		listDFS = self.getDFS()
	
		bFindCurrent = false
		
		if(!hasattr(self, "atomNodeInstructionPointer"))
		{
			bFindCurrent = true
		}
		else
		{
			if(self.atomNodeInstructionPointer == None)
			{
				bFindCurrent = true
			}
		}
		
		for i in range(listDFS.count())
		{
			atomNode = listDFS.get(i)
			
			if(bFindCurrent == true)
			{
				atomNodeReturn = atomNode
				break
			}
			
			if(self.atomNodeInstructionPointer == atomNode)
			{
				bFindCurrent = true
			}
		}
		
		return atomNodeReturn
	}
	
	def work(self, actor : Actor)
	{
		while(true)
		{
			atomNode = self.getSiblingAtomNode()
			self.atomNodeInstructionPointer = atomNode
			if(atomNode == None)
			{
				break
			}
			
			if(isinstance(atomNode.atom, YieldCommand))
			{
				break
			}
			
			atomNode.atom.execute(actor)
		}
	}
}

class ProgramInterface()
{
	def __init__(self, program : Program)
	{
		self.findAtomNode = program.findAtomNode
		self. getParentAtom = program.getParentAtom
	}
}

class Program()	
{
	def __init__(self)	
	{
		self.model = Model()
		self.functions = Functions()
	}
	
	def findAtomNode(self, atomType : AtomType, objectName : str)
	{
		atomNode = None
		
		if(atomType == Attribute)
		{
			atomNode = self.model.findAtomNode(objectName)
		}
		else
		{
			atomNode = self.functions.findAtomNode(objectName)
		}
		
		return atomNode
	}
	
	def getParentAtom(self, atom : Atom)
	{
		parentAtom = self.model.getParentAtom(atom)
		if(parentAtom == None)
		{
			parentAtom = self.functions.getParentAtom(atom)
		}
		
		return parentAtom
	}
}
class AtomBehaviour()
{
	def __init__(self, actor : Actor, atom : Atom, callbackFunc : function)
	{
		self.actor = actor
		self.atom = atom
		self.callbackFunc = callbackFunc
	}
	
	def call(self)
	{
		
	}
}

class YieldCommand(Command)	
{
}

class RecipeExecuter()
{
	def __init__(self, actor : Actor, listVar : list)
	{
		self.actor = actor
		self.listVar = listVar
		self.listProgram = list()
	
		for i in range(self.listVar.count())
		{
			var = self.listVar.get(i)
			var.signalPublish.connect(self.slotPublish)
		}
	
		self.assignProgram()
	}
	
	def assignProgram(self)
	{
		self.listProgram.clear()
		
		for i in range(self.listVar.count())
		{
			var = self.listVar.get(i)
			
			program = deserialize(var.data)
			self.listProgram.append(program)
		
			if(isinstance(program, Program))
			{
				listAttributeNode = program.model.getDFS()
				listCommandNode = program.functions.getDFS()
				
				for i in range(listAttributeNode.count())
				{
					node = listAttributeNode.get(i)
					node.atom.program = ProgramInterface(program)
				}
				
				for i in range(listCommandNode.count())
				{
					node = listCommandNode.get(i)
					node.atom.program = ProgramInterface(program)
				}
			}
		}
	}
	
	def slotPublish(self, dataMsg : AbstractExMsg, sender)
	{
		self.assignProgram()
	}
	
	def work(self)
	{
		for i in range(self.listProgram.count())
		{
			program = self.listProgram.get(i)
			
			if(isinstance(program, Program))	
			{
				program.functions.work(self.actor)
			}
		}
	}
}

{