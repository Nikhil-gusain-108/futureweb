from django.shortcuts import render,HttpResponse,redirect
from .models import Blog,Hotdrops,upcomingairdrops
from django.shortcuts import get_object_or_404
import asyncio
from asgiref.sync import sync_to_async
from .forms import Blogform
from django.contrib.auth.decorators import login_required
# Create your views here.
# Home
async def home(request):
	try:
		main = asyncio.create_task(MainBlog())
		dones = asyncio.create_task(upAirdrop())
		airdrop= asyncio.create_task(hotDrops())
		maindrops =await main
		done = await dones
		airdrops = await airdrop
		data = {"finished":done,"airdrops":airdrops}
		await sync_to_async(data.update)(maindrops)
		return await sync_to_async(render)(request,"apptemplates/index.html",data)
	except Exception as e:
		data = {"error":e,"type":type(e).__name__}
		return await sync_to_async(render)(request,"apptemplates/error.html",data)

# Blog page redirector
async def blog(request,blog_id):
	try:
		blog = asyncio.create_task(sync_to_async(get_object_or_404)(Blog,pk = blog_id))
		main= asyncio.create_task(MainBlog())
		blogs = await blog
		maindrops = await main
		data={"blog":blogs}
		data.update(maindrops)
		return await sync_to_async(render)(request,"apptemplates/blog.html",data)
	except Exception as e:
		data = {"error":e,"type":type(e).__name__}
		return await sync_to_async(render)(request,"apptemplates/error.html",data)

# All blogs page
async def all_blogs(request):
	try:
		blog = asyncio.create_task(sync_to_async(Blog.objects.all)())
		main= asyncio.create_task(MainBlog())
		blogs = await blog
		maindrops = await main
		data={"blog":blogs}
		data.update(maindrops)
		return await sync_to_async(render)(request,"apptemplates/allblogs.html",data)
	except Exception as e:
		data = {"error":e,"type":type(e).__name__}
		return await sync_to_async(render)(request,"apptemplates/error.html",data)

# function to add blog
@login_required
def add_blog(request):
    if request.method == 'POST':
        form = Blogform(request.POST, request.FILES)
        if form.is_valid():
            blog =form.save()
            return redirect('blog',blog_id = blog.id)
        else:
            return render(request, 'apptemplates/add_blog.html', {'form': form})
    else:
        form = Blogform()
        return render(request, 'apptemplates/addblog.html', {'form': form})
# ********************************************** Helper Function **********************************************

# Must Read Blogs & recent blogs
async def MainBlog():
	mustread = asyncio.create_task(sync_to_async(Blog.objects.filter)(Must_read=True)) 
	blog = asyncio.create_task(sync_to_async(Blog.objects.order_by)("Created_date"))
	imp = await mustread
	recent = await blog
	data = {
		"recent":recent,
		"imp":imp
	}
	return data

# Hot Airdops
@sync_to_async
def hotDrops():
 airdrops = Hotdrops.objects.all()
 return airdrops
# Completed Airdrops
@sync_to_async
def upAirdrop():
 airdrops = upcomingairdrops.objects.all()
 return airdrops