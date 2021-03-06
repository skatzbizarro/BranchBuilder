import logging
logging_setting = {
    "filename" : "logger",
    "level" : logging.DEBUG,
    "format" : '%(asctime)s %(message)s',
    "datefmt" : '%Y-%m-%d %H:%M:%S' 
}

site_url='http://honey-g/BranchBuilder'
jenkins_url='http://honey-g:8080'
per_page = 20
od_users = {
		"anisevich": {"full_name": "Alex Nisevich", "email": "anisevich@sugarcrm.com"} ,\
		"avucinic": {"full_name": "Andrija Vucinic", "email": "avucinic@sugarcrm.com"} ,\
		"betauser1": {"full_name": "Beta User1", "email": "quality-assurance@sugarcrm.com"} ,\
		"betauser2": {"full_name": "Beta User2", "email": "quality-assurance@sugarcrm.com"} ,\
		"cfox": {"full_name": "Chinghua Fox", "email": "cfox@sugarcrm.com"} ,\
        "crobinson": {"full_name": "Chian Robinson", "email":"crobinson@sugarcrm.com"} ,\
		"cyan": {"full_name": "Carmen Yan", "email": "cyan@sugarcrm.com"} ,\
		"cwang": {"full_name": "Joe Wang", "email": "cwang@sugarcrm.com"} ,\
		"dclunie": {"full_name": "David Clunie", "email": "dclunie@sugarcrm.com"} ,\
		"dsafar": {"full_name": "David Safar", "email": "dsafar@sugarcrm.com"} ,\
		"egan": {"full_name": "Emily Gan", "email": "egan@sugarcrm.com"} ,\
		"eyang": {"full_name": "Eric Yang", "email": "eyang@sugarcrm.com"} ,\
		"franklin": {"full_name": "Franklin Liu", "email": "franklin@sugarcrm.com"} ,\
		"ifleming": {"full_name": "Ian Fleming", "email": "ifleming@sugarcrm.com"} ,\
		"jimmy": {"full_name": "Jimmy Chen", "email": "jchen@sugarcrm.com"} ,\
		"gpatterson": {"full_name": "Geno Patterson", "email": "gpatterson@sugarcrm.com"} ,\
		"grelampagos": {"full_name": "Gino Relampagos", "email": "gpatterson@sugarcrm.com"} ,\
		"jchen": {"full_name": "Jackie Chen", "email": "chenj@sugarcrm.com"} ,\
		"jcho": {"full_name": "Jessica Cho", "email": "jcho@sugarcrm.com"} ,\
		"jxia": {"full_name": "Jennifer Xia", "email": "jxia@sugarcrm.com"} ,\
		"mlouis": {"full_name": "Mazen Louis", "email": "mlouis@sugarcrm.com"} ,\
		"oyang": {"full_name": "Oliver Yang", "email": "oyang@sugarcrm.com"} ,\
		"rlee": {"full_name": "Randy Lee", "email": "rlee@sugarcrm.com"} ,\
		"rsennewald": {"full_name": "Ray Sennewald", "email": "rsennewald@sugarcrm.com"} ,\
		"rzhou": {"full_name": "Ran Zhou", "email": "rzhou@sugarcrm.com"} ,\
		"rchugh": {"full_name": "Rahul Chugh", "email": "rchugh@sugarcrm.com"} ,\
		"sharmaa": {"full_name": "Ajay Sharma", "email": "sharmaa@sugarcrm.com"} ,\
		"support1": {"full_name": "Support 1", "email": "support@sugarcrm.com"} ,\
		"support2": {"full_name": "Support 2", "email": "support@sugarcrm.com"} ,\
		"support3": {"full_name": "Support 3", "email": "support@sugarcrm.com"} ,\
		"support4": {"full_name": "Support 4", "email": "support@sugarcrm.com"} ,\
		"support5": {"full_name": "Support 5", "email": "support@sugarcrm.com"} ,\
		"phuang": {"full_name": "Paul Huang", "email": "phuang@sugarcrm.com"} ,\
		"pgarg": {"full_name": "Praveen Garg", "email": "pgarg@sugarcrm.com"} ,\
		"rgupta": {"full_name": "Rohit Gupta", "email": "rgupta@sugarcrm.com"} ,\
		"sarya": {"full_name": "Stuti Arya", "email": "sarya@sugarcrm.com"}, \
		"rtayal": {"full_name": "Rahul Tayal", "email": "rtayal@sugarcrm.com"}, \
		"asinha": {"full_name": "Amarendra Sinha", "email": "asinha@sugarcrm.com"}, \
		"ajabble": {"full_name": "Ashish Jabble", "email": "ajabble@sugarcrm.com"}, \
		"mshariq": {"full_name": "Mohammed Shariq", "email": "mshariq@sugarcrm.com"}, \
		"msharma": {"full_name": "Monika Sharma", "email": "rma@sugarcrm.com"}, \
		"rthakur": {"full_name": "Raj Thakur", "email": "rthakur@sugarcrm.com"}, \
		"asharma": {"full_name": "Akshat Sharma", "email": "asharma@sugarcrm.com"}, \
		"bchandak": {"full_name": "Basant Chandak", "email": "bchandak@sugarcrm.com"}, \
		"msehra": {"full_name": "Mukul Sehra", "email": "msehra@sugarcrm.com"}, \
		"sgupta": {"full_name": "Sanket Gupta", "email": "sgupta@sugarcrm.com"}, \
		"sparsuram": {"full_name": "Suresh Parsuram", "email": "sparsuram@sugarcrm.com"}, \
		"sjaideep": {"full_name": "Sandhya Jaideep", "email": "sjaideep@sugarcrm.com"}, \
		"etrue": {"full_name": "Ellen True", "email": "etrue@sugarcrm.com"}, \
		"hwon": {"full_name": "Haley Won", "email": "hwon@sugarcrm.com"}, \
		"ikakouris": {"full_name": "Iliana Kakouris", "email": "ikakouris@sugarcrm.com"}, \
		"jshaheen": {"full_name": "Jill Shaheen", "email": "jshaheen@sugarcrm.com"}, \
		"sbarthwal": {"full_name": "Siddharth Barthwal", "email": "sbarthwal@sugarcrm.com"}, \
		"guptas": {"full_name": "Shikher Gupta", "email": "guptas@sugarcrm.com"}, \
		"dghani": {"full_name": "Dilshad Ghani", "email": "dghani@sugarcrm.com"}, \
		"vjakhwal": {"full_name": "Vinisha Jakhwal", "email": "vjakhwal@sugarcrm.com"}, \
		"gnanda": {"full_name": "Gourav Nanda", "email": "gnanda@sugarcrm.com"}, \
		"dkumar": {"full_name": "Dinesh Kumar", "email": "dkumar@sugarcrm.com"}, \
		"hsingh": {"full_name": "Hitendra Singh", "email": "hsingh@sugarcrm.com"}, \
		"rbhatnagar": {"full_name": "Ruchi Bhatnagar", "email": "rbhatnagar@sugarcrm.com"}
	}
od_users["tester"] =  {"full_name": "QA Tester", "email": "oyang@sugarcrm.com"}
od_version = [
    '6.5.18',
    '6.5.19',
    '6.5.20',
    '6.6.1',
    '6.6.2',
    '6.6.3',
    '6.7.7',
    '6.7.8',
    '6.7.9',
    '6.7.10',
    '7.2.2.1',
    '7.2.2.2',
    '7.2.2.3',
    '7.5.0.0',
    '7.5.0.1',
    '7.5.1.0',
    '7.5.2.0',
    '7.6.0.0',
    '7.6.0.0RC1',
    '7.6.0.0RC2',
    '7.6.0.0RC3',
    '7.6.0.0RC4',
    '7.6.0.0rbv',
    '7.7.0.0'
]
ci_users = dict(od_users)
ci_version = od_version

nomad_users = {
		"builder": {"full_name": "Branch Builder", "email": "build@sugarcrm.com"} , \
	}
nomad_version = ['6.7.1']
nomad_flavors = ['Ult', 'Ent', 'Crop', 'Pro']
builds_dir = "/var/www/public/builds"
kue_server = "http://honey-g:3000"
