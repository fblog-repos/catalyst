
import builder,os
from catalyst_support import *

class generic_sparc(builder.generic):
	"abstract base class for all sparc builders"
	def __init__(self,myspec):
		builder.generic.__init__(self,myspec)
		self.settings["mainarch"]="sparc"
		if self.settings["hostarch"]=="sparc64":
			if not os.path.exists("/bin/linux32"):
				raise CatalystError,"required /bin/linux32 executable not found (\"emerge setarch\" to fix.)"
			self.settings["CHROOT"]="linux32 chroot"
		else:
			self.settings["CHROOT"]="chroot"

class arch_sparc(generic_sparc):
	"builder class for generic sparc (sun4cdm)"
	def __init__(self,myspec):
		generic_sparc.__init__(self,myspec)
		self.settings["CFLAGS"]="-O2 -pipe"
		self.settings["CXXFLAGS"]="-O2 -pipe"
		self.settings["CHOST"]="sparc-unknown-linux-gnu"

def register(foo):
	"Inform main catalyst program of the contents of this plugin."
	foo.update({"sparc":arch_sparc})
