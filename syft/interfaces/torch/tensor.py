import syft

class IntTensor(object):

	def __init__(self,data=None,syft_obj=None):
		if(syft_obj is None):
			self.syft_obj = syft.IntTensor(data)
		else:
			self.syft_obj = syft_obj

	def __getitem__(self,i):
		out = self.syft_obj.to_numpy()[i]
		if(out.shape == ()):
			return int(out)
		else:
			return IntTensor(out)

	def __repr__(self):
		return self.syft_obj.__repr__()

class FloatTensor(object):

	def __init__(self,data=None,syft_obj=None):
		if(syft_obj is None):
			self.syft_obj = syft.FloatTensor(data)
		else:
			self.syft_obj = syft_obj
	
	def index_select(self,dim,indices):
		return FloatTensor(syft_obj=self.syft_obj.index_select(dim,indices.syft_obj))

	def softmax(self,dim=-1):
		return FloatTensor(syft_obj=self.syft_obj.softmax())

	def float(self):
		return self

	def unsqueeze(self, dim=0):
		return FloatTensor(syft_obj=self.syft_obj.unsqueeze(dim))

	def sample(self, dim = -1):
		return IntTensor(syft_obj=self.syft_obj.sample(dim))

	def __repr__(self):
		return self.syft_obj.__repr__()