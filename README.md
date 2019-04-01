'''
a = SQL().PATH('../sql.db').TABLE('sql').UPDATE(ip='10.194.160111.6').TARGET(ID='29').RUN()
a = SQL().PATH('../sql.db').TABLE('sql').FIND(ip='10.194.160111.6').RUN()
a = SQL().PATH('../sql.db').TABLE('sql').ADD(ip='10.194.160111.6').RUN()
a = SQL().PATH('../sql.db').TABLE('sql').DELETE(ip='10.194.160111.6').RUN()

'''