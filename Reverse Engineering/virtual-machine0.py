from __future__ import division
import struct

outputTeeth = 40
inputTeeth = 8
inputRPM = 39722847074734820757600524178581224432297292490103995912415595360101562905
def getOutputRPM(inputRPM, inputTeeth, outputTeeth):
  GR = int(outputTeeth/inputTeeth)
  return inputRPM * GR
  
outputRPM = getOutputRPM(inputRPM, inputTeeth, outputTeeth)

# NOTE: I could not get the long_to_bytes function from Crypto.Util to work
# on my machine, so to save time I just used the source code

#####  THE FOLLOWING CODE WAS NOT MADE BY ME AND IS PROVIDED FROM A MODULE!  #####
#####    Full name of function's source: Crypto.Util.number.long_to_bytes    #####
def long_to_bytes(n, blocksize=0):
  """Convert a positive integer to a byte string using big endian encoding.
  
  If :data:`blocksize` is absent or zero, the byte string will
  be of minimal length.
  
  Otherwise, the length of the byte string is guaranteed to be a multiple
  of :data:`blocksize`. If necessary, zeroes (``\\x00``) are added at the left.
  
  .. note::
      In Python 3, if you are sure that :data:`n` can fit into
      :data:`blocksize` bytes, you can simply use the native method instead::
  
          >>> n.to_bytes(blocksize, 'big')
  
      For instance::
  
          >>> n = 80
          >>> n.to_bytes(2, 'big')
          b'\\x00P'
  
      However, and unlike this ``long_to_bytes()`` function,
      an ``OverflowError`` exception is raised if :data:`n` does not fit.
  """
  
  if n < 0 or blocksize < 0:
      raise ValueError("Values must be non-negative")
  
  result = []
  pack = struct.pack
  
  # Fill the first block independently from the value of n
  bsr = blocksize
  while bsr >= 8:
      result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
      n = n >> 64
      bsr -= 8
  
  while bsr >= 4:
      result.insert(0, pack('>I', n & 0xFFFFFFFF))
      n = n >> 32
      bsr -= 4
  
  while bsr > 0:
      result.insert(0, pack('>B', n & 0xFF))
      n = n >> 8
      bsr -= 1
  
  if n == 0:
      if len(result) == 0:
          bresult = b'\x00'
      else:
          bresult = b''.join(result)
  else:
      # The encoded number exceeds the block size
      while n > 0:
          result.insert(0, pack('>Q', n & 0xFFFFFFFFFFFFFFFF))
          n = n >> 64
      result[0] = result[0].lstrip(b'\x00')
      bresult = b''.join(result)
      # bresult has minimum length here
      if blocksize > 0:
          target_len = ((len(bresult) - 1) // blocksize + 1) * blocksize
          bresult = b'\x00' * (target_len - len(bresult)) + bresult
  
  return bresult
######## Crypto.Util.number.long_to_bytes ########

byte_string = long_to_bytes(outputRPM)
message = byte_string.decode("latin-1")
print(message)
