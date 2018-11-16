import admin
		
hiro_privileges = ["make a user tea", "give user criptic life advice", "not ever die"]
admin_hiro = admin.Admin("hiro", "uncle", 64, "firenation",  "jasmintea", hiro_privileges)
admin_hiro.privileges.show_privileges()
