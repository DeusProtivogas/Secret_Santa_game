from apscheduler.schedulers.asyncio import AsyncIOScheduler

schebuler = AsyncIOScheduler()
schebuler.add_job(planned_addition_of_points, trigger="date",
                          next_run_time=data, kwargs={'user': user, 'id_user': CHAT_ID,
                                                      'data': data, 'points': month_points})
schebuler.start()