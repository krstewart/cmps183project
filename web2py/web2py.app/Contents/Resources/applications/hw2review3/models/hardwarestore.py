# -*- coding: utf-8 -*-
db = DAL('sqlite://storage.db')

db.define_table('product',
          Field('quantity_on_hand', 'integer'),
          Field('price', 'double'),
          Field('quantity_on_order', 'integer')
  )

db.define_table('contacts',
          Field('name', 'string'),
          Field('phone', 'string'),
          Field('email', 'string'),
          Field('notes', 'text')
  )

db.define_table('supplier',
          Field('name', 'string'),
          Field('address', 'string'),
          Field('owner_id', 'reference contacts'),
          format='%(name)s'
  )

db.define_table('customer',
          Field('name', 'string'),
          Field('phone', 'string'),
          Field('email', 'string'),
          Field('owner_id', 'reference product'),
          format='%(name)s'
  )

db.define_table('purchase',
          Field('Date_', 'date'),
          Field('items_purchased', 'string'),
          Field('price_of_item', 'double'),
          Field('quantity', 'integer'),
          Field('total_purchase', 'double')
  )
