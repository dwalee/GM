#default password
password = 'Onstar123456789!'

#create list collect users' info
z_id = list()
first = list()
last = list()
u_email = list()

#create list to create gaa roles for user(s)
gaa_role_of_choice = list()

#open user role file and collect the gaa roles for user
gaa_roles_file = open('user role.txt', "r+")
all_gaa_roles = gaa_roles_file.read().split("\n")
all_roles_len = len(all_gaa_roles)
for i in range(all_roles_len):
	role = all_gaa_roles[i]
	gaa_role_of_choice.append(role)
	#print(gaa_role_of_choice[i])
gaa_roles_file.close()

user_info_file = open('users_info.txt', "r+")
all_users = user_info_file.read().split("\n")
all_len = len(all_users)
for i in range(all_len):
	info = all_users[i].split("\t")
	z_id.append(info[0])
	first.append(info[1])
	last.append(info[2])
	u_email.append(info[3])
user_info_file.close()

reporting_group_file = open('Reporting_Group.txt', "r+")
reporting_group = reporting_group_file.read()
gaa_roles_file.close()