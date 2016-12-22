from conans import ConanFile

class FlowExtra(ConanFile):
	name = "FlowExtra"
	version = "bleed"
	description = """Contains predefined components and utilities which could be useful when using Flow."""
	url = "https://github.com/CynaraKrewe/Flow"
	license = "MIT"
	author = "Mathias Spiessens"
	exports = "*"
	build_policy = "missing"
	requires = "FlowCore/bleed@cynara/testing"
	
	def source(self):
		self.run("git clone https://github.com/CynaraKrewe/Flow.git")

	def build(self):
		self.output.info("Nothing to build, this package provides sources.")

	def package(self):
		self.copy("components.*", "flow", "Flow/flow")
		self.copy("debug.*", "flow", "Flow/flow")
		self.copy("utility.h", "flow", "Flow/flow")