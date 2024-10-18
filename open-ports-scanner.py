import socket
import subprocess
import asyncio
from datetime import datetime
import concurrent.futures



def try_port(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((remoteServerIP, port))

	sock.settimeout(None)
	if result == 0:
		print(f' <<< Port {port} is open >>> ', end='', flush=True)
	else:
		sock.close()
	return (port, result)


subprocess.call('clear', shell=True)
remoteServer = input('Enter ip: ')
remoteServerIP = socket.gethostbyname(remoteServer)
print(f'\nscanning on {remoteServerIP}\n')

t1 = datetime.now()


async def main():
	with concurrent.futures.ThreadPoolExecutor(max_workers=1017) as executor:
		loop = asyncio.get_event_loop()
		futures = [
			loop.run_in_executor(
				executor,
				try_port,
				i
			)
			for i in range(22, 65535)
		]
		results = await asyncio.gather(*futures)
		print('\n\n')
		for response in results:
			if response[1] == 0:
				print(f'port {response[0]}: \t open')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())


