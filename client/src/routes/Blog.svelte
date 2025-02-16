<script>
    const data = {summaries:[
	{
		post: 'welcome',
		title: 'Welcome to the Aperture Science computer-aided enrichment center',
		content:
			['We hope your brief detention in the relaxation vault has been a pleasant one.',
				'Your specimen has been processed and we are now ready to begin the test proper.',
				'### Some notes:',
				'- Try to relax',
				'- Take your meds',
				'- Get some sleep',
			]

	},
	{
		post: 'safety',
		title: 'Safety notice',
		content:
			['While safety is one of many Enrichment Center Goals, the Aperture Science High Energy Pellet, seen to the left of the chamber, can and has caused permanent disabilities, such as vaporization. Please be careful.',
				'','Find out more at [google](http://google.com/search?q=more)']
	},

	{
		post: 'cake',
		title: 'This was a triumph',
		content: ["I'm making a note here: HUGE SUCCESS.", 'Massive, just the **BEST** thing ever!']
	},
	{
		post: 'daniella',
		title: 'Daniella - Friend or foe?',
		content: ["Friends don't let friends watch Gordon Ramsey, so _she's_ fo sho in the foe zone."]
	},

	{
		post: 'lorem',
		title: 'Lorem ipsum',
		content:
			['_Lorem_ **ipsum** `dolor` sit amet, consectetur adipiscing elit. Suspendisse eget odio et odio viverra porttitor',
				'nec ac ante. Nunc eleifend maximus eros nec pellentesque. Cras viverra velit eu justo efficitur, id lacinia',
				'odio semper. Vivamus ullamcorper suscipit sapien, ut congue enim accumsan nec. Integer quam `dolor`, vestibulum',
				'at aliquam id, eleifend id turpis. Vestibulum consequat _lorem_ eu pharetra mattis. Nulla iaculis sapien',
				'eu `dolor` viverra, eleifend luctus leo scelerisque. Vestibulum ante **ipsum** primis in faucibus orci luctus',
				'et ultrices posuere cubilia curae; Vestibulum interdum, tellus vel sollicitudin gravida, **ipsum** quam imperdiet',
				'lectus, quis dapibus neque metus sit amet leo.',
				'',
				'```\nPraesent tempor feugiat quam quis fermentum. Aenean dui nunc, malesuada eget mi non, auctor eleifend ante.',
				'In et congue nibh, ac feugiat arcu. Pellentesque habitant morbi tristique senectus et netus et ',
				'fames ac turpis egestas. Suspendisse bibendum neque quis risus posuere luctus eget quis nisi. Phasellus',
				'ultricies suscipit risus ut suscipit. Ut lobortis lacus ac ultricies convallis. Aenean egestas, ex at laoreet',
				'ultricies, risus dui facilisis purus, eu laoreet libero purus vitae **ipsum**. Phasellus orci magna, sollicitudin',
				'et velit quis, viverra ultricies `dolor`. Interdum et malesuada fames ac ante **ipsum** primis in faucibus.',
				'```\n',
				'Suspendisse non fermentum sem. Nullam purus turpis, sollicitudin in eros ac, tristique egestas quam. Quisque',
				'eleifend ante quis pharetra faucibus. Phasellus vel nulla vitae est tristique tincidunt. Curabitur semper',
				'volutpat purus rhoncus mollis. Pellentesque faucibus sapien odio. Donec et arcu tincidunt purus rhoncus',
				'viverra vel eu lacus.',
				'',
				'Phasellus aliquet varius tellus sit amet imperdiet. Fusce finibus orci felis, vitae maximus enim blandit',
				'non. Fusce et orci laoreet ante pellentesque sagittis a vel metus. Suspendisse vulputate sem vitae vehicula',
				'varius. In egestas, augue non varius convallis, _lorem_ tellus consectetur nunc, a elementum ante mauris non',
				'purus. Vivamus vel est vitae felis porttitor lacinia non vel nunc. Nullam laoreet lacus odio, vitae convallis',
				'enim aliquam at. Pellentesque pulvinar luctus feugiat. Integer in tempus leo. Nunc ac ante tristique justo',
				'convallis hendrerit eu quis justo. Etiam convallis eget nibh at hendrerit.',
				'',
				'Pellentesque dictum auctor turpis lobortis blandit. Morbi nec lacus elit. Aenean ligula `dolor`, malesuada',
				'vitae odio in, sollicitudin elementum odio. Donec non enim et ligula porta luctus a sed velit. Mauris scelerisque',
				'nibh eu nibh tincidunt pretium. Pellentesque vel ligula venenatis, suscipit quam et, facilisis purus.',
				'Aliquam tempus posuere ornare. Donec ut sagittis tortor, id mollis mi. In et ex nulla. Nam laoreet sapien',
				'neque, non interdum mi ornare in. Maecenas eget tempus est. Praesent eleifend ut purus a commodo. Cras',
				'ultricies velit et tempor malesuada. Proin fermentum libero ac diam eleifend, vel eleifend ligula scelerisque.',
				'Aliquam aliquam fringilla luctus. In id justo nibh.']
	},
	{
		post: 'markdown',
		title: 'Writing Markdown',
		hidden:true,
		content:['**Some examples of markdown:**',
			'',
			'Entering | Produces',
			'--- | ---',
            ' `# Heading` | # Heading',

			'',
			'Produces:',
			'',
			'Heading',
			'=======',
			'',
			'Entering:',
			'',
			'```',
			'Sub-heading',
			'-----------',
			'```',
			'',
			'Produces:',
			'',
			'Sub-heading',
			'-----------',
			'',
			'Entering:',
			'',
			'```',
			'# Alternative heading',
			'```',
			'',
			'Produces:',
			'',
			'# Alternative heading']

// # Alternative heading

// ## Alternative sub-heading

// Paragraphs are separated 
// by a blank line.

// Two spaces at the end of a line  
// produce a line break."
	}
]};

</script>
<h1>Blog</h1>
<ul>
	{#each data.summaries as {post, title}}
		<li><a href='/blog/{post}'>{title}</a></li>
	{/each}
</ul>