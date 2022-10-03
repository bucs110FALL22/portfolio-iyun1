plot="A French narrator (Tom Kenny) introduces an aquatic city known as Bikini Bottom containing an ecstatic, hyperactive, optimistic, naive, and friendly sponge named SpongeBob SquarePants. SpongeBob gets ready to apply for a job as the fry cook at the Krusty Krab, much to the annoyance of the restaurant's cashier and SpongeBob's grumpy neighbor, an octopus named Squidward Tentacles. SpongeBob initially reconsiders his decision on the perceived count that he is not good enough, until his best friend, a starfish named Patrick Star, convinces him otherwise. Humored with SpongeBob's gullibility and enthusiasm, both Squidward and the restaurant's owner, a crab named Mr. Eugene Krabs, decide to manipulate SpongeBob by sending him on an impossible errand to purchase a seemingly rare, high-caliber spatula. The two believe Spongebob is unqualified, and conclude that he will not return. Soon after Spongebob's departure, five buses containing ravenous anchovies stop at the Krusty Krab, all furiously demanding meals. Unable to satisfy the anchovies' hunger, Squidward and Mr. Krabs are left to deal with the unsatisfied crowd. The anchovies start piling up, forcing Squidward and Mr. Krabs to flee to the top of a support pole. Squidward and Mr. Krabs both believe that they are hopeless and about to be killed by the large mob. SpongeBob surprises the two by returning from his errand, having bought a spatula perfectly matching Mr. Krabs' specifications, which he uses to speedily cook Krabby Patties for all the anchovies. After the mob subsides, SpongeBob is officially welcomed as a Krusty Krab employee, much to Squidward's dismay. After Mr. Krabs leaves to count the day's profits, Patrick arrives and orders a Krabby Patty, and is hurled from the establishment upon a mostly unseen, and audibly manic, reprise of SpongeBob's cooking feat. The pilot ends with Squidward calling for Mr. Krabs in the hopes of getting SpongeBob in trouble for the presumed mess he has created."


plotchanges={
  "SpongeBob SquarePants":"Ahoy Spongeboy!", 
  "job":"Oppertunistic Output",
  "Spongebob":"Spongeboy",
  "Krab":"Cheapskate",
  "Mr. Krabs":"Cheapy the Cheapskate"
}

for key,values in plotchanges.items():
  article=plot.replace(key, values)
print(article)