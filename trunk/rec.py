import sys
sys.path.append('./aux/')

from try_ import * 
from select_interface import MyFrame as MySelect

from pylab import *
import wx
import os


app = wx.PySimpleApp()


wildcard = "All files (*.*)|*.*"
dlg = wx.FileDialog(None, "Open sketch file...", os.getcwd(), style=wx.OPEN, wildcard=wildcard)
if dlg.ShowModal() == wx.ID_OK:
	filename = dlg.GetPath()
	dlg.Destroy()

	holo=imread(filename)

	### fourier_transform
	TF = fftshift(fft2(fftshift(holo)))


	### spatial_filter
	sketch = MySelect( log(abs(TF)) )	
	if sketch.ShowModal()==wx.ID_OK:
		mask0 = where(sketch.mask>0,1,0)
		TF_filter = TF*mask0

		### inverse_fourier_transform
		ITF = fftshift(ifft2(fftshift(TF_filter)))
	
		figure(), imshow(abs(ITF)), gray()
		figure(), imshow(angle(ITF)), gray()
	
		### Propagacion
		propagate_window = Propagate_WIndow(None,-1,"",im=ITF)
		if propagate_window.ShowModal()==wx.ID_OK:
			field=propagate_window.im
			propagate_window.Destroy()
		
			figure(), imshow(abs(field)), gray()
			figure(), imshow(angle(field)), gray()
		#~ 
	
			

		
