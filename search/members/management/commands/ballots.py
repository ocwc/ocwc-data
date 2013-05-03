# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from joomla.models import *
import datetime

def main():
	ballots_ids = [10, 11]

	# for bid in ballots_ids:
	# 	ballot = JosElectionBallots.objects.get(pk=bid)
		
	# 	# print dir(ballot)
	# 	voters = []
	# 	for boption in ballot.joselectionballotoptions_set.all():
	# 		# print unicode(boption), boption.joselectionvotes_set.count()

	# 		for vote in boption.joselectionvotes_set.all():
	# 			crmid = int(vote.crm_id.id)
	# 			if crmid not in voters:
	# 				voters.append(crmid)
	# 				# print crmid, 
	# 				print vote.crm_id.first_name, vote.crm_id.last_name.encode('utf-8')

	# 	# print sorted(voters)
	# 	print ballot.title, len(voters)

	for candidate in JosElectionCandidates.objects.filter(election_year=2013):
		c = candidate.crmid_candidate
		j = JosUsers.objects.get(pk=c.external_identifier)
		
		print c.first_name, c.last_name, j.username, j.email


class Command(BaseCommand):
    help = "calculates ballots"

    def handle(self, *args, **options):
        main()
