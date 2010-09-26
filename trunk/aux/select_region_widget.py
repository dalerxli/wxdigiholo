import  wx



class Select(wx.Window):
	
	def __init__(self, parent, id=-1, bmp=None, size=None):
		
		self.flag_DoubleClick=False
		self.p = None
		self.clist=[]
		self.all_list=[]
		self.flag_select=None	
		wx.Window.__init__(self, parent, id,size=(640,640),style=wx.SUNKEN_BORDER)


		self.x = self.y = 0


		if bmp==None:
			self.maxWidth=640
			self.maxHeight=480
			img = wx.EmptyImage(self.maxWidth,self.maxHeight)
			self.bmp=wx.BitmapFromImage(img)
		else:
			self.bmp=bmp	
			self.maxWidth  = size[0]
			self.maxHeight = size[1]



		self.buffer = wx.EmptyBitmap(self.maxWidth, self.maxHeight)
		dc = wx.BufferedDC(None, self.buffer)
		dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
		dc.Clear()
		self.DoDrawing(dc)

		self.Bind(wx.EVT_PAINT, self.OnPaint)
		self.Bind(wx.EVT_LEFT_UP, self.OnMouseUp)
		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick)


		self.flag_DCLICK=False
		


	def OnPaint(self, event):	

		dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)


		if self.p is None: return
		
		
		dc.SetBrush(wx.Brush(wx.Color(0, 0, 0), wx.TRANSPARENT))
		dc = wx.PaintDC(self)

		
		if self.flag_select==None:
			self.clist=[]
			return
		

		elif self.flag_select=='manual':	
		### select points

			dc.SetPen(wx.Pen('GREEN', 4))
			for point in self.clist:
				dc.DrawCircle(point.x,point.y, 1) 


	def OnDoubleClick(self, event):
		self.flag_DoubleClick=True	
		dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)
		dc.SetPen(wx.Pen('RED', 4))
	

		if self.all_list:
			self.clist=self.clist[1::]


		for k in range(len(self.clist)):
			dc.DrawLine(self.clist[k].x, self.clist[k].y, self.clist[k-1].x, self.clist[k-1].y)
	

		###dc.DrawPolygon(self.clist)	

		self.all_list.append(self.clist)
		
		self.clist=[]


	def if_flag_DoubleClick_is_False(self):
		self.all_list.append(self.clist)


	def cancel(self):
		self.clist=[]
		self.all_list=[]
		dc = wx.BufferedDC(None, self.buffer)
		self.DoDrawing(dc)
		self.Refresh()



	def DoDrawing(self, dc, printing=False):
		dc.DrawBitmap(self.bmp, 0, 0, True)


	def OnMouseDown(self, event):
		self.SetCursor(wx.StockCursor(wx.CURSOR_CROSS))
		self.Refresh()	

	def OnMouseUp(self, event):
		self.SetCursor(wx.StockCursor(wx.CURSOR_PENCIL))
		self.p = event.GetPosition()		
		self.clist.append(self.p)
		self.flag_DCLICK=None	
		self.Refresh()
		
		
class SketchFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, -1, "Sketch Frame", size=(640,480))
		self.sketch = Select(self, -1)
		self.sketch.flag_select='manual'


if __name__ == '__main__':
	app = wx.PySimpleApp()
	frame = SketchFrame(None)
	frame.Show(True)
	app.MainLoop()
	
	




