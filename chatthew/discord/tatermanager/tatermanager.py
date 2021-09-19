from datetime import datetime
from datetime import timedelta
import json

class TaterManager:
    def __init__(self, client):
        # Two objects:
        # one is indexed from user - time
        # the second is indexed by time - list of users
        # the user - time one is checked to see if user will be kicked
        # the time - list of users one is used to kick
        # user: time
        # {
        #  user1: time1,
        #  user2: time2
        # }
        #  time1: [user1, user2],
        #  time2: [user3, user4]
        # {
        #
        # TODO: make thread safe due to async code
        # problem case: interleaved kick and resubscribe
        # TODO: make persistent through restart
        self.kick_list = {}
        self.time_kick_list = {}
        self.kick_lock = None
        with open('tatermanager.json') as f:
            self.raw_config = json.load(f)
        self.server_id = self.raw_config['serverID']
        self.subscriber_id = self.raw_config['subscriberID']
        self.potato_id = self.raw_config['potatoID']
        self.exempt_list = self.raw_config['exemptList']
        self.kick_delta = self.raw_config['kickDelta']
        pass

    def kick(self):
        pass

    def schedule_kick(self, kick_time):
        pass

    def add_to_kick_list(self, mid):
        # ToDO: check if already in
        kick_time = datetime.now() + timedelta(days=self.kick_delta)
        self.kick_list[mid] = kick_time
        if kick_time in self.time_kick_list:
            self.time_kick_list[kick_time].push(mid)
        else:
            self.time_kick_list[kick_time] = [mid]
            self.schedule_kick(kick_time)
        return

    def clear_from_kick_list(self, mid):
        if mid in self.kick_list:
            time = self.kick_list[mid]
            self.kick_list.pop(mid)
            self.time_kick_list[time].remove(mid)
            if len(self.time_kick_list[time]) == 0:
                pass

    def check_member(self, before, after):
        mid = before.id
        # if in the exemption list, roles don't matter
        if mid not in self.exempt_list:
            if self.has_improper_roles(after):
                self.add_to_kick_list(mid)
            elif mid in self.kick_list:
                self.clear_from_kick_list(mid)


    def has_improper_roles(self, member):
        has_potato = False
        has_subscriber = False
        for role in member.roles:
            rid = role.id
            has_potato = True if rid == self.potato_id else has_potato
            has_subscriber = True if rid == self.subscriber_id else has_subscriber
            # this could technically terminate early but with few roles
            # improvement is possibly negligible
        return has_potato and not has_subscriber
