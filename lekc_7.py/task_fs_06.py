# удаляем каталоги даже если там внутри есть каталоги
import shutil

shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
