import os
import shutil
import sys

input_file = os.path.join(
    os.getenv('MESON_BUILD_ROOT'),
    os.getenv('MESON_SUBDIR'),
    sys.argv[1])

output_file = os.path.join(
    os.getenv('MESON_SOURCE_ROOT'),
    os.getenv('MESON_SUBDIR'),
    sys.argv[2])

print(input_file)
print(output_file)
print(os.path.dirname(output_file))
os.makedirs(os.path.dirname(output_file), exist_ok=True)
shutil.copyfile(input_file, output_file)
