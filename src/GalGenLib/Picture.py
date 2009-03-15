# Copyright (c) 2009 Stepan Seycek. All rights reserved.
# 
# Redistribution and use in source and binary forms, with or 
# without modification, are permitted provided that the following 
# conditions are met:
# 
#  1. Redistributions of source code must retain the above 
#     copyright notice, this list of conditions and the 
#     following disclaimer.
#  2. Redistributions in binary form must reproduce the above 
#     copyright notice, this list of conditions and the following 
#     disclaimer in the documentation and/or other materials 
#     provided with the distribution.
#  3. All advertising materials mentioning features or use of this 
#     software must display the following acknowledgement: 
#     “This product includes software developed by Stepan Seycek.”
#  4. The name Stepan Seycek may not be used to endorse or promote 
#     products derived from this software without specific prior 
#     written permission. 
#
# THIS SOFTWARE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY 
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL 
# THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, 
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR 
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
# OF THE POSSIBILITY OF SUCH DAMAGE. 

from Modifyable import Modifyable
from PictureReference import PictureReference
from Contained import Contained
from PictureHTMLOutputter import PictureHTMLOutputter

class Picture(Modifyable, PictureReference, Contained):

    def __init__(self, name, pic_location, menu_id, title, subtitle):
        Modifyable.__init__(self)
        PictureReference.__init__(self, name, pic_location, menu_id, title, subtitle)
        Contained.__init__(self)

    def save(self, stream):
        self.__writeStartTag(stream)
        self.__writeEndTag(stream)

    def __writeStartTag(self, stream):
        stream.write(u'<picture name="%s" location="%s" menu-id="%s" title="%s" subtitle="%s">\n'
                     % (self.name, self.pic_location, self.menu_id, self.title, self.subtitle))

    def __writeEndTag(self, stream):
        stream.write(u'</picture>\n')

    def _getHtmlPath(self):
        return '%s/%s/%s' % (self.parent.parent.name, self.parent.name, self.html_file_name)

    def generateOutput(self, target_dir, progress_updater, page_index):
        page_index += 1
        progress_updater.update(page_index, '%s: %s' % (self.__class__.__name__, self.name))
        outputter = PictureHTMLOutputter(self)
        return outputter.generateOutput(target_dir, progress_updater, page_index)
    
