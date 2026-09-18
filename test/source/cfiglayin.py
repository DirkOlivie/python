'''
     https://docs.python.org/3/tutorial/classes.html
'''
class CFigLayin:
    def __init__(self, contour_levels_type='free', title='', xrange=[-1.,-1.], yrange=[-1.,-1.], xtype='', ytype='', legendlocation='', filetype='png' ,code='', colorscheme='tableau', ysplit='',figsize=[6,6], csvoutput=False, regionintitle=False):
        self.contour_levels_type = contour_levels_type
        self.title= title
        self.xrange=xrange
        self.yrange=yrange
        self.xtype=xtype
        self.ytype=ytype
        self.legendlocation=legendlocation
        self.code = code
        self.filetype = filetype
        self.colorscheme = colorscheme
        self.ysplit= ysplit
        self.figsize= figsize
        self.csvoutput=csvoutput
        self.regionintitle=regionintitle
