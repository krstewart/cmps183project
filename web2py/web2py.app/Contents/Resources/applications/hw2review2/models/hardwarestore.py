db.define_table('category', Field('name'))

db.define_table('products',
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                Field('quantity', 'integer', requires=IS_NOT_EMPTY()),
                Field('price', 'integer', requires=IS_NOT_EMPTY()),
                Field('supplier', 'list:reference supplier'),
                format = '%(name)s')

db.define_table('purchase',
                Field('products', 'list:reference products'),
                Field('quantity', 'list:integer', requires=IS_NOT_EMPTY()),
                Field('price', 'integer', requires=IS_NOT_EMPTY()),
                auth.signature)

db.define_table('contact',
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                Field('phone_number', 'integer', requires=IS_NOT_EMPTY()),
                Field('email', 'string'),
                Field('description', 'string', requires=IS_NOT_EMPTY()),
                format = '%(name)s')

db.define_table('customer',
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                Field('phone_number', 'integer', requires=IS_NOT_EMPTY()),
                Field('email', 'string'),
                format = '%(name)s')

db.define_table('supplier',
                Field('name', 'string', requires=IS_NOT_EMPTY()),
                Field('address', 'string', requires=IS_NOT_EMPTY()),
                Field('contact', 'list:reference contact'),
                format = '%(name)s')
