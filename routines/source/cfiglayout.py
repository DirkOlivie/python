'''
     https://docs.python.org/3/tutorial/classes.html
'''
class CFigLayout:
    def __init__(self, contour_levels_type='free', title='', xrange=[-1.,-1.], yrange=[-1.,-1.], xtype='', ytype='', xlabel=None, legendlocation='', filetype='png' ,code='', colorscheme='tableau', ysplit='',figsize=[6,6], csvoutput=False, regionintitle=False, plotdir=None, axhline=None, axvline=None, axhspan=None, axvspan=None, axhlinestyle='dashed', axvlinestyle='dashed'):
        self.contour_levels_type = contour_levels_type
        self.title= title
        self.xrange=xrange
        self.yrange=yrange
        self.xtype=xtype
        self.ytype=ytype
        self.xlabel=xlabel
        self.legendlocation=legendlocation
        self.code = code
        self.filetype = filetype
        self.colorscheme = colorscheme
        self.ysplit= ysplit
        self.figsize= figsize
        self.csvoutput=csvoutput
        self.regionintitle=regionintitle
        self.plotdir=plotdir
        self.axhline=axhline
        self.axvline=axvline
        self.axhspan=axhspan
        self.axvspan=axvspan
        self.axhlinestyle=axhlinestyle
        self.axvlinestyle=axvlinestyle
