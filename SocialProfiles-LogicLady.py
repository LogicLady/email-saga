import pandas
from intercom.client import Client
intercom = Client(personal_access_token='dG9rOjQ2MmM2MzlkXzQwNzRfNGVkYl84YjYwXzkwZDVmNzcyMzcyMjoxOjA=')

emailsdf = pandas.DataFrame(pandas.read_csv('intercomemailsin.csv'))

twitter=[]; twitterurl=[]; facebook=[]; facebookurl=[]; klout=[]
klouturl=[]; vimeo=[]; vimeourl=[]; linkedin=[]; linkedinurl=[]
googleplus=[]; googleplusurl=[]; flickr=[]; flickrurl=[]; github=[]
githuburl=[]; foursquare=[]; foursquareurl=[]; youtube=[]; youtubeurl=[]
myspace=[]; myspaceurl=[]; tumblr=[]; tumblrurl=[]; wordpress=[]
wordpressurl=[]; other=[]; otherurl=[]; othertype=[]; avatarurl=[]
jobtitle=[]

emailnum = 0; twitternum = 0; facebooknum = 0; linkedinnum = 0
kloutnum = 0; vimeonum = 0; googleplusnum = 0; flickrnum = 0
githubnum = 0; foursquarenum = 0; youtubenum = 0; myspacenum = 0
tumblrnum = 0; wordpressnum = 0; othernum = 0

for each in emailsdf['Email']:
	intercom.users.create(email=each)
	search = intercom.users.find(email=each)
	
	avatarurl.append(search.avatar.image_url)
	
	if len(search.custom_attributes) > 0:
		attr = str(search.custom_attributes)
		jobtitle.append(attr[15:len(attr)-2])
	else: jobtitle.append("")

	for profile in search.social_profiles:
		if profile.name == 'Twitter':
			twitter.append(profile.username); twitterurl.append(profile.url)
			twitternum = twitternum + 1
		elif profile.name == 'Facebook':
			facebook.append(profile.username); facebookurl.append(profile.url)
			facebooknum = facebooknum + 1
		elif profile.name == 'Klout':
			klout.append(profile.username); klouturl.append(profile.url)
			kloutnum = kloutnum + 1
		elif profile.name == 'Vimeo':
			vimeo.append(profile.username); vimeourl.append(profile.url)
			vimeonum = vimeonum + 1
		elif profile.name == 'LinkedIn':
			linkedin.append(profile.username); linkedinurl.append(profile.url)
			linkedinnum = linkedinnum + 1
		elif profile.name == 'GooglePlus':
			googleplus.append(profile.username); googleplusurl.append(profile.url)
			googleplusnum = googleplusnum + 1
		elif profile.name == 'Flickr':
			flickr.append(profile.username); flickrurl.append(profile.url)
			flickrnum = flickrnum + 1
		elif profile.name == 'Github':
			github.append(profile.username); githuburl.append(profile.url)
			githubnum = githubnum + 1
		elif profile.name == 'Foursquare':
			foursquare.append(profile.username); foursquareurl.append(profile.url)
			foursquarenum = foursquarenum + 1
		elif profile.name == 'YouTube':
			youtube.append(profile.username); youtubeurl.append(profile.url)
			youtubenum = youtubenum + 1
		elif profile.name == 'Myspace':
			myspace.append(profile.username); myspaceurl.append(profile.url)
			myspacenum = myspacenum + 1
		elif profile.name == 'Tumblr':
			tumblr.append(profile.username); tumblrurl.append(profile.url)
			tumblrnum = tumblrnum + 1
		elif profile.name == 'Wordpress':
			wordpress.append(profile.username); wordpressurl.append(profile.url)
			wordpressnum = wordpressnum + 1
		else:
			other.append(profile.username); otherurl.append(profile.url); othertype.append(profile.name)
			othernum = othernum + 1

	
	if len(twitter) == emailnum: twitter.append("") 
	if len(twitterurl) == emailnum: twitterurl.append("")	
	if len(facebook) == emailnum: facebook.append("")
	if len(facebookurl) == emailnum: facebookurl.append("")
	if len(klout) == emailnum: klout.append("")	
	if len(klouturl) == emailnum: klouturl.append("")		
	if len(vimeo) == emailnum: vimeo.append("")
	if len(vimeourl) == emailnum: vimeourl.append("")
	if len(linkedin) == emailnum: linkedin.append("")	
	if len(linkedinurl) == emailnum: linkedinurl.append("")	
	if len(googleplus) == emailnum: googleplus.append("")
	if len(googleplusurl) == emailnum: googleplusurl.append("")
	if len(flickr) == emailnum: flickr.append("")
	if len(flickrurl) == emailnum: flickrurl.append("")
	if len(github) == emailnum: github.append("")
	if len(githuburl) == emailnum: githuburl.append("")
	if len(foursquare) == emailnum: foursquare.append("")
	if len(foursquareurl) == emailnum: foursquareurl.append("")
	if len(youtube) == emailnum: youtube.append("")
	if len(youtubeurl) == emailnum: youtubeurl.append("")
	if len(myspace) == emailnum: myspace.append("")
	if len(myspaceurl) == emailnum: myspaceurl.append("")
	if len(tumblr) == emailnum: tumblr.append("")
	if len(tumblrurl) == emailnum: tumblrurl.append("")
	if len(wordpress) == emailnum: wordpress.append("")
	if len(wordpressurl) == emailnum: wordpressurl.append("")
	if len(other) == emailnum: other.append("")	
	if len(otherurl) == emailnum: otherurl.append("")
	if len(othertype) == emailnum: othertype.append("")

	emailnum = emailnum + 1

print("# Emails: \t\t" + str(len(emailsdf.index)))
print("# Twitter Accounts:\t" + str(twitternum))
print("# Facebook Accounts:\t" + str(facebooknum))
print("# LinkedIn Accounts:\t" + str(linkedinnum))
print("# Klout Accounts:\t" + str(kloutnum))
print("# Vimeo Accounts:\t" + str(vimeonum))
print("# Google Plus Accounts:\t" + str(googleplusnum))
print("# Flickr Accounts:\t" + str(flickrnum))
print("# GitHub Accounts:\t" + str(githubnum))
print("# FourSquare Accounts:\t" + str(foursquarenum))
print("# YouTube Accounts:\t" + str(youtubenum))
print("# MySpace Accounts:\t" + str(myspacenum))
print("# Tumblr Accounts:\t" + str(tumblrnum))
print("# WordPress Accounts:\t" + str(wordpressnum))
print("# Other Accounts:\t" + str(othernum))


emailsdf['Twitter Username'] = pandas.Series(twitter)
emailsdf['Twitter URL'] = pandas.Series(twitterurl)
emailsdf['Facebook Username'] = pandas.Series(facebook)
emailsdf['Facebook URL'] = pandas.Series(facebookurl)
emailsdf['LinkedIn Username'] = pandas.Series(linkedin)
emailsdf['LinkedIn URL'] = pandas.Series(linkedinurl)
emailsdf['Klout Username'] = pandas.Series(klout)
emailsdf['Klout URL'] = pandas.Series(klouturl)
emailsdf['Vimeo Username'] = pandas.Series(vimeo)
emailsdf['Vimeo URL'] = pandas.Series(vimeourl)
emailsdf['Google Plus Username'] = pandas.Series(googleplus)
emailsdf['Google Plus URL'] = pandas.Series(googleplusurl)
emailsdf['Flickr Username'] = pandas.Series(flickr)
emailsdf['Flickr URL'] = pandas.Series(flickrurl)
emailsdf['GitHub Username'] = pandas.Series(github)
emailsdf['GitHub URL'] = pandas.Series(githuburl)
emailsdf['FourSquare Username'] = pandas.Series(foursquare)
emailsdf['FourSquare URL'] = pandas.Series(foursquareurl)
emailsdf['YouTube Username'] = pandas.Series(youtube)
emailsdf['YouTube URL'] = pandas.Series(youtubeurl)
emailsdf['MySpace Username'] = pandas.Series(myspace)
emailsdf['MySpace URL'] = pandas.Series(myspaceurl)
emailsdf['Tumblr Username'] = pandas.Series(tumblr)
emailsdf['Tumblr URL'] = pandas.Series(tumblrurl)
emailsdf['Other Username'] = pandas.Series(other)
emailsdf['Other URL'] = pandas.Series(otherurl)
emailsdf['Other Type'] = pandas.Series(othertype)
emailsdf['Avatar URL'] = pandas.Series(avatarurl)
emailsdf['Job Title'] = pandas.Series(jobtitle)
emailsdf.to_csv('intercomemailsin.csv',index=False)	

#for user in intercom.users.all():
#	print(user.email)