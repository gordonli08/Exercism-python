class Bucket:
    def __init__(self, capacity, content, name):
        self.capacity = capacity
        self.content = content
        self.name = name

#input:
#L in bucket 1
#L in bucket 2
#L to reach
#"one" or "two" to decide which bucket to fill first
#output:
#moves taken to reach desired L
#"one" or "two" representing which bucked holds the desired Ls
#L left in other bucket
def measure(bucket_one, bucket_two, goal, start_bucket):
    step = 1
    if start_bucket == "one":
        pourer = Bucket(bucket_one, bucket_one, "one")
        rec = Bucket(bucket_two, 0, "two")
    else:
        pourer = Bucket(bucket_two, bucket_two, "two")
        rec = Bucket(bucket_one, 0, "one")
    
    if rec.capacity == goal:
        rec.content = rec.capacity
        step += 1

    #print(f"step:{step}, pourer:{pourer.content}, rec:{rec.content}")
    while (pourer.content != goal and rec.content != goal):
        if rec.content == rec.capacity:
            rec.content = 0
        elif pourer.content == 0:
            pourer.content = pourer.capacity
        else:
            poured = pourer.content + rec.content
            rec.content = poured if poured <= rec.capacity else rec.capacity
            pourer.content = poured - rec.content
        step += 1
        #print(f"step:{step}, pourer:{pourer.content}, rec:{rec.content}")
    
    return ((step, pourer.name, rec.content)
        if pourer.content == goal
        else (step, rec.name, pourer.content))
