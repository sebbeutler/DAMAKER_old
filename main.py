# %%

# import os
# os.environ['JAVA_HOME'] = 'C:/Program Files/Java/jdk-11.0.13'
# os.environ["JAVA_HOME"] = "C:/Users/PC/anaconda3/envs/dmk/Library" 

import damaker 

# ImageStack loading

stack = damaker.load('resources/E1.tif') # Should be 3-dimensionnal for 'Pixel intensity'

stack = stack.clone(stack.data[1])      # Keep channel n°2 only (created as a distinct copy)

print(stack)


# Image processing tools

from damaker import processing

out = processing.pixelIntensity(stack)
print(out)


# Pipeline

# Operations setup

op1 = damaker.Operation('Pixel intensity')
op1.set(input=stack)

op2 = damaker.Operation('Invert colors')
op2.set(input=stack)

def my_routine():
    print('>> Running my routine')

# Execution

p = damaker.Pipeline()

p.queue(op1)
p.queue(op2)
p.queue(my_routine)
p.run()

# Equivalent to
# p.queue(op1).queue(op2).queue(my_routine).run()

# Result

print('\n\n'+'  Output  '.center(50, "#"))
print(op1.output)
print(op2.output)

damaker.close() # (Optional)

# %%
