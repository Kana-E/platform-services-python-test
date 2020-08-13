from handlers.rewards_handler import RewardsHandler, Init, CustomerData, CustomerSummary

#define endpoint settings
url_patterns = [
    #test that this works
    (r'/', Init),
    (r'/rewards', RewardsHandler),
    (r'/info', CustomerData),
    (r'/summary', CustomerSummary)
]
