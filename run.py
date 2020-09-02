import teacherbot
import os

test = teacherbot.bot(command_prefix='test.',
                      current_guild=675806001231822863,
                      current_channel=750573479249707078,
                      token=os.environ['testing_token'])
