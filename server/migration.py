"""
    Database migration
    Set up the initial db content and amend as required
    Any method with the migrate decorator is run if not called before according to the 'migrated' collection
"""
from config import settings
import sqlite3 
from datetime import datetime

db = None
migrated = None
migrate_funcs = []

def migrate(func):
    migration = func.__name__

    def wrapper(*args, **kwargs):
        if migration in migrated:
            return

        print('Migration: ' + migration)
        func(*args, **kwargs)
        params = (migration, datetime.now().isoformat())
        #print(params)
        db.execute('insert into migrated (migration, timestamp) values (?, ?)', params)
        #db.commit()
    # add the wrapper to the list of migrations
    # if it hasn't already been called, then it will
    # be called once and recorded in the database
    migrate_funcs.append(wrapper)
    return func


def update_database(path):
    global db, migrated
    db = sqlite3.connect(path, autocommit=True)

    # the first time this runs, migrated table does not exist:
    try:
        migrated = [x[0] for x in db.execute('select migration from migrated').fetchall()]
        print(migrated)
    except: 
        db.execute('create table migrated(migration, timestamp)')
        migrated = []
    for func in migrate_funcs:
        func()
    print('db up to date')


@migrate
def create_articles():
	db.execute('create table articles (link, title, content, released, permission)')
	db.execute('create unique index idx_article_link on articles (link)')

	articles = [
	{
	"link": "thought-20250216",
	"title": "Thought for the Day - 16/02/2025",
	"content": [
	"We are all aware of the importance of our health and wellbeing and we",
	"know the golden rules; eat healthily, exercise daily, try to have restful",
	"nights and manage your stress. Keep your body and mind in balance",
	"and all will be well.\n",
	"So, we decide to eat healthily. We can read about myriad diets, the",
	"advantages and disadvantages of different food types, but we rarely",
	"register how our food choices have a profound impact on our mood,",
	"energy and concentration.",
	"Daily physical activity has many positive health benefits, however, as we",
	"get older it gets more important to have different types of exercise that",
	"address our needs; cardio exercise to help with our heart health,",
	"strength exercise to keep our bones strong, flexibility exercise to reduce",
	"injuries, and balance exercise to prevent falls.",
	"There are debates about the “necessary” hours for sleep. Nevertheless,",
	"if we have a bad night sleep, we not only feel tired, but we can’t focus,",
	"and our memory is less reactive. This is because while we are asleep",
	"our brain works hard; sorting out the information we were confronted",
	"with during the day and refreshing our memory.",
	"Managing stress is one of the most difficult tasks we face in our busy",
	"world as no one can escape it. Different calming techniques are",
	"recommended – breathing exercise, yoga, meditation. In my experience",
	"a positive mindset is key to address stressful situations.\n",
	"As a health coach, I believe that every individual has unique health and",
	"wellbeing needs. Accountability ensures that a healthy lifestyle is the",
	"result. Coaching supports and encourages those who chose to embark",
	"on a wellbeing journey to achieve their goals in the most effective way",
	"possible.",
	],
	"released": True,
	"permission": ""
	},
	{
	"link": "safety",
	"title": "Safety notice",
	"content": [
	"While safety is one of many **Enrichment Center Goals**, the [Aperture Science High Energy Pellet](/programme), seen to the left of the chamber, can and has caused permanent disabilities, such as vaporization. Please be careful.",
	"",
	"Find out more at [google](http://google.com/search?q=more)",
	],
	"released": True,
	"permission": 'ADMIN'
	},
	{
	"link": "cake",
	"title": "This was a triumph",
	"content": [
	"I'm making a note here: HUGE SUCCESS.",
	"Massive, just the **BEST** thing ever!",
	],
	"released": False
	},
	{
	"link": "daniella",
	"title": "Daniella - Friend or foe?",
	"content": [
	"Friends don't let friends watch Gordon Ramsey, so _she's_ fo sho in the foe zone.",
	],
	"released": False
	},
	{
	"link": "lorem",
	"title": "Lorem ipsum",
	"content": [
	"_Lorem_ **ipsum** `dolor` sit amet, consectetur adipiscing elit. Suspendisse eget odio et odio viverra porttitor",
	"nec ac ante. Nunc eleifend maximus eros nec pellentesque. Cras viverra velit eu justo efficitur, id lacinia",
	"odio semper. Vivamus ullamcorper suscipit sapien, ut congue enim accumsan nec. Integer quam `dolor`, vestibulum",
	"at aliquam id, eleifend id turpis. Vestibulum consequat _lorem_ eu pharetra mattis. Nulla iaculis sapien",
	"eu `dolor` viverra, eleifend luctus leo scelerisque. Vestibulum ante **ipsum** primis in faucibus orci luctus",
	"et ultrices posuere cubilia curae; Vestibulum interdum, tellus vel sollicitudin gravida, **ipsum** quam imperdiet",
	"lectus, quis dapibus neque metus sit amet leo.",
	"",
	"```\nPraesent tempor feugiat quam quis fermentum. Aenean dui nunc, malesuada eget mi non, auctor eleifend ante.",
	"In et congue nibh, ac feugiat arcu. Pellentesque habitant morbi tristique senectus et netus et ",
	"fames ac turpis egestas. Suspendisse bibendum neque quis risus posuere luctus eget quis nisi. Phasellus",
	"ultricies suscipit risus ut suscipit. Ut lobortis lacus ac ultricies convallis. Aenean egestas, ex at laoreet",
	"ultricies, risus dui facilisis purus, eu laoreet libero purus vitae **ipsum**. Phasellus orci magna, sollicitudin",
	"et velit quis, viverra ultricies `dolor`. Interdum et malesuada fames ac ante **ipsum** primis in faucibus.",
	"```\n",
	"Suspendisse non fermentum sem. Nullam purus turpis, sollicitudin in eros ac, tristique egestas quam. Quisque",
	"eleifend ante quis pharetra faucibus. Phasellus vel nulla vitae est tristique tincidunt. Curabitur semper",
	"volutpat purus rhoncus mollis. Pellentesque faucibus sapien odio. Donec et arcu tincidunt purus rhoncus",
	"viverra vel eu lacus.",
	"",
	"Phasellus aliquet varius tellus sit amet imperdiet. Fusce finibus orci felis, vitae maximus enim blandit",
	"non. Fusce et orci laoreet ante pellentesque sagittis a vel metus. Suspendisse vulputate sem vitae vehicula",
	"varius. In egestas, augue non varius convallis, _lorem_ tellus consectetur nunc, a elementum ante mauris non",
	"purus. Vivamus vel est vitae felis porttitor lacinia non vel nunc. Nullam laoreet lacus odio, vitae convallis",
	"enim aliquam at. Pellentesque pulvinar luctus feugiat. Integer in tempus leo. Nunc ac ante tristique justo",
	"convallis hendrerit eu quis justo. Etiam convallis eget nibh at hendrerit.",
	"",
	"Pellentesque dictum auctor turpis lobortis blandit. Morbi nec lacus elit. Aenean ligula `dolor`, malesuada",
	"vitae odio in, sollicitudin elementum odio. Donec non enim et ligula porta luctus a sed velit. Mauris scelerisque",
	"nibh eu nibh tincidunt pretium. Pellentesque vel ligula venenatis, suscipit quam et, facilisis purus.",
	"Aliquam tempus posuere ornare. Donec ut sagittis tortor, id mollis mi. In et ex nulla. Nam laoreet sapien",
	"neque, non interdum mi ornare in. Maecenas eget tempus est. Praesent eleifend ut purus a commodo. Cras",
	"ultricies velit et tempor malesuada. Proin fermentum libero ac diam eleifend, vel eleifend ligula scelerisque.",
	"Aliquam aliquam fringilla luctus. In id justo nibh.",
	],
	"released": False
	},
	{
	"link": "markdown",
	"title": "Writing Markdown",
	"content": [
	"**Some examples of markdown:**",
	"",
	"Entering | Produces",
	"--- | ---",
	" `# Heading` | # Heading",

	"",
	"Produces:",
	"",
	"Heading",
	"=======",
	"",
	"Entering:",
	"",
	"```",
	"Sub-heading",
	"-----------",
	"```",
	"",
	"Produces:",
	"",
	"Sub-heading",
	"-----------",
	"",
	"Entering:",
	"",
	"```",
	"# Alternative heading",
	"```",
	"",
	"Produces:",
	"",
	"# Alternative heading",
	"",
	"```",
	"## Alternative sub-heading",
	"```",
	"",
	"Produces:",
	"",
	"## Alternative sub-heading",
	"",
	"```",
	"Paragraphs are separated",
	"by a blank line.",
	"",
	"Two spaces at the end of a line  ",
	"produce a line break.",
	"```",
	"",
	"Produces:",
	"",
	"Paragraphs are separated",
	"by a blank line.",
	"",
	"Two spaces at the end of a line  ",
	"produce a line break."
	],
	"released": True
	},
	]	
	# all the content needs to be single string:
	for x in articles:
		x["content"] = "\n".join(x["content"])
		x["permission"] = x.get("permission", "")
	db.executemany('insert into articles (link, title, content, released, permission) values (:link, :title, :content, :released, :permission)', articles)

@migrate
def create_testimonials():
	db.execute('create table testimonials (name, date, statement)')

	testimonials = [
		{
        	"name": "Daddy",
          	"date": '20001216',
        	'statement': "It just doesn't get better"
		},
		{
        	"name": "Shadow",
          	"date": '20170214',
        	'statement': "Woof!"
		},
		{
        	"name": "Daniella",
          	"date": '20050512',
        	'statement': "Mummy is lovely, very lovely"
		},
		{
        	"name": "Sandra",
          	"date": '20020424',
        	'statement': "Do my bidding!"
		}
	]	

	db.executemany('insert into testimonials (name, date, statement) values (:name, :date, :statement)', testimonials)

@migrate
def create_users():
	db.execute('create table users (email, name, permission)')
	db.execute('create unique index idx_user_email on users (email)')
	users = [
		{
        	"email": "william.norman.walker@gmail.com",
          	"name": 'William',
        	'permission': "ADMIN"
		},
		{
        	"email": "andrea.norman.walker@gmail.com",
          	"name": 'Andrea',
        	'permission': "ADMIN COACH"
		},
		{
        	"email": "daniella.norman.walker@gmail.com",
          	"name": 'Daniella',
			"permission": ""
		}
	]
	db.executemany('insert into users (email, name, permission) values (:email, :name, :permission)', users)

@migrate
def create_emails():
	db.execute('create table email_templates (name, subject, content)')
	db.execute('create unique index idx_email_template_name on email_templates (name)')

	email_templates = [
		{
			"name": "SIGN_IN",
			"subject": "Sign in Authorisation",
			"content": "Hi {name}, your sign in is authorised, click [here]{link} to continue."
		},
		{
			"name": "WELCOME",
			"subject": "Welcome to Resilence4Health",
			"content": "Hi {name} and welcome to Resilence4Health."
		},
	]
	db.executemany('insert into email_templates (name, subject, content) values (:name, :subject, :content)', email_templates)

# finally we run when main: 
if __name__ == "__main__":
    update_database(settings['databaseName'])
