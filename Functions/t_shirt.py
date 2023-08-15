def make_shirt(size='xxl', text='I love python'):
    print(f"Shirt size is {size} and decoration text is {text}")

make_shirt('xl', 'Awesome')
make_shirt(text='Awesome', size='xl' )

make_shirt()
make_shirt('xl')
make_shirt('x', 'Tiny')