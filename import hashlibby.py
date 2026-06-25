import hashlib

n_curve = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

     # The input string is stored in `input_str`
parts = input_str.split("Derived CA Rules")[1:9]  # 8 blocks

resonance_values = []
     for block_str in parts:
         # Split into lines
         lines = block_str.splitlines()
         block_bytes = bytearray()
         for line in lines:
             line = line.strip()
             if line.startswith('[[') and line.endswith(']]'):
                 # Remove the brackets
                 inner = line[2:-2]
                 nums = inner.split(',')
                 if len(nums) != 8:
                     # Skip if not 8 numbers
                     continue
                 try:
                     for num in nums:
                         # Convert each number string to integer
                         b = int(num.strip())
                         if b < 0 or b > 255:
                             # Invalid byte, skip this rule? but we take as mod 256?
                             b = b % 256
                         block_bytes.append(b)
                 except:
                     pass
         # We may have more or less than 512 bytes? We require 512.
         if len(block_bytes) < 512:
             # Pad with zeros to 512
             block_bytes.extend([0] * (512 - len(block_bytes)))
         elif len(block_bytes) > 512:
             block_bytes = block_bytes[:512]

         h = hashlib.sha256(block_bytes)
         digest = h.digest()  # 32 bytes
         resonance = int.from_bytes(digest[:4], 'big')
         resonance_values.append(resonance)

     # Multiply all resonance values modulo n_curve
     priv_key = 1
     for r in resonance_values:
         if r == 0:
             r = 1
         priv_key = (priv_key * r) % n_curve

     priv_key_hex = hex(priv_key)
