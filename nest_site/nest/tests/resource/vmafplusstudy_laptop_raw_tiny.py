dataset_name = 'VMAF_Plus_DB'
yuv_fmt = 'yuv420p'
width = 1920
height = 1080

# quality_width = 1280
# quality_height = 720
# resampling_type = 'lanczos'

# quality_width = 720
# quality_height = 480
# resampling_type = 'lanczos'

ref_score = 100.0

ref_videos = [{'content_id': 0,
  'content_name': 'BarbieLife_B',
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/BarbieLife_B_ref.yuv'},
 {'content_id': 1,
  'content_name': 'BeautifulGirls_A',
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/BeautifulGirls_A_ref.yuv'},
 {'content_id': 2,
  'content_name': 'Bloodline_A',
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/Bloodline_A_ref.yuv'},
]

dis_videos = [{'asset_id': 1000,
  'content_id': 0,
  'os': {'andrewp': 89.0,
         'andyc': 80.0,
         'aschuler': 49.0,
         'asinghal': 68.0,
         'btorres': 100.0,
         'caleb': 88.0,
         'cwilms': 81.0,
         'czhao': 90.0,
         'ddenlinger': 79.0,
         'decsobiel@gmail.com': 96.0,
         'devenson@catflix.com': 96.0,
         'dteoh': 98.0,
         'hjagadeesan': 59.0,
         'jingxian@sranford.edu': 60.0,
         'kalvey': 94.0,
         'kchen@catflix.com': 96.0,
         'lfriedman@catflix.com': 84.0,
         'mangalap': 88.0,
         'mariakaz': 100.0,
         'mrobbe': 96.0,
         'msemeniakin': 48.0,
         'mufford': 64.0,
         'rbrodie': 100.0,
         'rgallardo': 92.0,
         'rly': 88.0,
         'rsharma': 92.0,
         'rwaters': 81.0,
         'sdearaujo': 91.0,
         'sdu@catflix.com': 96.0,
         'sfedorov@catflix.com': 95.0,
         'ssharma': 93.0,
         'svenkatrav@catflix.com': 58.0,
         'tgoodall@catflix.com': 90.0,
         'thuang': 67.0,
         'vyelevich': 96.0,
         'wwolcott': 94.0,
         'zchen': 88.0,
         'zli': 96.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/BarbieLife_B_ref.yuv'},
 {'asset_id': 1001,
  'content_id': 1,
  'os': {'andrewp': 85.0,
         'andyc': 87.0,
         'aschuler': 77.0,
         'btorres': 41.0,
         'caleb': 93.0,
         'cwilms': 81.0,
         'czhao': 79.0,
         'ddenlinger': 74.0,
         'decsobiel@gmail.com': 56.0,
         'devenson@catflix.com': 78.0,
         'dteoh': 65.0,
         'hjagadeesan': 83.0,
         'jingxian@sranford.edu': 81.0,
         'kalvey': 100.0,
         'kchen@catflix.com': 73.0,
         'lfriedman@catflix.com': 84.0,
         'mangalap': 93.0,
         'mariakaz': 89.0,
         'mrobbe': 93.0,
         'msemeniakin': 91.0,
         'mufford': 64.0,
         'rbrodie': 93.0,
         'rgallardo': 85.0,
         'rly': 91.0,
         'rsharma': 63.0,
         'rwaters': 74.0,
         'sdearaujo': 86.0,
         'sdu@catflix.com': 74.0,
         'sfedorov@catflix.com': 85.0,
         'ssharma': 89.0,
         'svenkatrav@catflix.com': 51.0,
         'tgoodall@catflix.com': 100.0,
         'thuang': 76.0,
         'timothy.l.robinson@comcast.net': 76.0,
         'yjayaraman': 85.0,
         'zchen': 85.0,
         'zli': 66.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/BeautifulGirls_A_ref.yuv'},
 {'asset_id': 1002,
  'content_id': 2,
  'os': {'andrewp': 98.0,
         'andyc': 82.0,
         'aprakash@catflix.com': 75.0,
         'aschuler': 82.0,
         'btorres': 95.0,
         'caleb': 97.0,
         'cwilms': 89.0,
         'czhao': 89.0,
         'ddenlinger': 68.0,
         'decsobiel@gmail.com': 92.0,
         'devenson@catflix.com': 61.0,
         'dteoh': 97.0,
         'hjagadeesan': 76.0,
         'jingxian@sranford.edu': 75.0,
         'kalvey': 99.0,
         'kchen@catflix.com': 91.0,
         'lfriedman@catflix.com': 70.0,
         'mangalap': 73.0,
         'mariakaz': 98.0,
         'mrobbe': 90.0,
         'msemeniakin': 96.0,
         'mufford': 86.0,
         'rbrodie': 98.0,
         'rgallardo': 91.0,
         'rly': 84.0,
         'rsharma': 91.0,
         'rwaters': 100.0,
         'sdearaujo': 93.0,
         'sdu@catflix.com': 90.0,
         'sfedorov@catflix.com': 98.0,
         'ssharma': 90.0,
         'thuang': 80.0,
         'timothy.l.robinson@comcast.net': 100.0,
         'vyelevich': 92.0,
         'wwolcott': 95.0,
         'yjayaraman': 81.0,
         'zchen': 89.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/ref_yuv/Bloodline_A_ref.yuv'},
 {'asset_id': 3,
  'content_id': 0,
  'os': {'andrewp': 80.0,
         'andyc': 65.0,
         'czhao': 92.0,
         'ddenlinger': 74.0,
         'devenson@catflix.com': 98.0,
         'dteoh': 80.0,
         'jingxian@sranford.edu': 53.0,
         'kalvey': 83.0,
         'lfriedman@catflix.com': 52.0,
         'mangalap': 36.0,
         'mrobbe': 95.0,
         'msemeniakin': 72.0,
         'rbrodie': 85.0,
         'rgallardo': 94.0,
         'rsharma': 91.0,
         'svenkatrav@catflix.com': 47.0,
         'wwolcott': 100.0,
         'zchen': 75.0,
         'zli': 89.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_1280x720_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 6,
  'content_id': 0,
  'os': {'aschuler': 53.0,
         'asinghal': 62.0,
         'btorres': 40.0,
         'caleb': 89.0,
         'cwilms': 82.0,
         'decsobiel@gmail.com': 97.0,
         'hjagadeesan': 78.0,
         'kchen@catflix.com': 98.0,
         'mariakaz': 86.0,
         'mufford': 64.0,
         'rly': 69.0,
         'rwaters': 79.0,
         'sdearaujo': 100.0,
         'sdu@catflix.com': 96.0,
         'sfedorov@catflix.com': 93.0,
         'ssharma': 83.0,
         'tgoodall@catflix.com': 100.0,
         'thuang': 52.0,
         'vyelevich': 89.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_1920x1080_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 11,
  'content_id': 0,
  'os': {'aschuler': 1.0,
         'caleb': 4.0,
         'ddenlinger': 22.0,
         'devenson@catflix.com': 11.0,
         'hjagadeesan': 10.0,
         'jingxian@sranford.edu': 1.0,
         'kalvey': 1.0,
         'kchen@catflix.com': 11.0,
         'lfriedman@catflix.com': 1.0,
         'mangalap': 17.0,
         'rbrodie': 1.0,
         'rly': 35.0,
         'rwaters': 1.0,
         'sdearaujo': 24.0,
         'sdu@catflix.com': 3.0,
         'sfedorov@catflix.com': 14.0,
         'svenkatrav@catflix.com': 9.0,
         'tgoodall@catflix.com': 1.0,
         'wwolcott': 32.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_320x240_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 13,
  'content_id': 0,
  'os': {'andrewp': 11.0,
         'andyc': 23.0,
         'asinghal': 20.0,
         'btorres': 3.0,
         'cwilms': 6.0,
         'czhao': 17.0,
         'decsobiel@gmail.com': 14.0,
         'dteoh': 4.0,
         'mariakaz': 15.0,
         'mrobbe': 1.0,
         'msemeniakin': 1.0,
         'mufford': 42.0,
         'rgallardo': 35.0,
         'rsharma': 49.0,
         'ssharma': 1.0,
         'thuang': 2.0,
         'vyelevich': 17.0,
         'zchen': 12.0,
         'zli': 12.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_384x288_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 14,
  'content_id': 0,
  'os': {'aschuler': 18.0,
         'caleb': 79.0,
         'cwilms': 35.0,
         'ddenlinger': 55.0,
         'decsobiel@gmail.com': 74.0,
         'hjagadeesan': 58.0,
         'jingxian@sranford.edu': 33.0,
         'kalvey': 74.0,
         'kchen@catflix.com': 41.0,
         'mangalap': 32.0,
         'mariakaz': 81.0,
         'rgallardo': 71.0,
         'rly': 75.0,
         'rwaters': 29.0,
         'sdearaujo': 65.0,
         'sfedorov@catflix.com': 74.0,
         'ssharma': 24.0,
         'svenkatrav@catflix.com': 52.0,
         'tgoodall@catflix.com': 75.0,
         'vyelevich': 38.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_512x384_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 15,
  'content_id': 0,
  'os': {'asinghal': 58.0,
         'btorres': 16.0,
         'caleb': 44.0,
         'cwilms': 43.0,
         'dteoh': 38.0,
         'jingxian@sranford.edu': 42.0,
         'lfriedman@catflix.com': 61.0,
         'mariakaz': 49.0,
         'mrobbe': 39.0,
         'msemeniakin': 62.0,
         'mufford': 43.0,
         'rbrodie': 2.0,
         'rgallardo': 63.0,
         'rly': 65.0,
         'rwaters': 25.0,
         'sdearaujo': 53.0,
         'svenkatrav@catflix.com': 47.0,
         'vyelevich': 41.0,
         'zchen': 41.0,
         'zli': 52.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_512x384_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 16,
  'content_id': 0,
  'os': {'andrewp': 22.0,
         'andyc': 32.0,
         'aschuler': 5.0,
         'btorres': 27.0,
         'czhao': 34.0,
         'devenson@catflix.com': 31.0,
         'hjagadeesan': 29.0,
         'kalvey': 34.0,
         'kchen@catflix.com': 31.0,
         'lfriedman@catflix.com': 1.0,
         'mangalap': 57.0,
         'rbrodie': 15.0,
         'rsharma': 43.0,
         'sdu@catflix.com': 35.0,
         'sfedorov@catflix.com': 24.0,
         'svenkatrav@catflix.com': 22.0,
         'thuang': 3.0,
         'wwolcott': 19.0,
         'zli': 43.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_512x384_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 17,
  'content_id': 0,
  'os': {'andrewp': 65.0,
         'andyc': 65.0,
         'aschuler': 33.0,
         'asinghal': 75.0,
         'caleb': 88.0,
         'ddenlinger': 57.0,
         'decsobiel@gmail.com': 64.0,
         'devenson@catflix.com': 85.0,
         'hjagadeesan': 61.0,
         'kchen@catflix.com': 87.0,
         'mrobbe': 50.0,
         'mufford': 51.0,
         'rbrodie': 78.0,
         'rwaters': 78.0,
         'sdu@catflix.com': 62.0,
         'thuang': 13.0,
         'vyelevich': 86.0,
         'zli': 79.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_720x480_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 18,
  'content_id': 0,
  'os': {'andrewp': 58.0,
         'asinghal': 59.0,
         'btorres': 40.0,
         'czhao': 63.0,
         'decsobiel@gmail.com': 64.0,
         'devenson@catflix.com': 70.0,
         'dteoh': 30.0,
         'mangalap': 27.0,
         'msemeniakin': 64.0,
         'rgallardo': 64.0,
         'rly': 83.0,
         'rsharma': 71.0,
         'sfedorov@catflix.com': 79.0,
         'ssharma': 16.0,
         'tgoodall@catflix.com': 81.0,
         'thuang': 9.0,
         'wwolcott': 42.0,
         'zchen': 53.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_720x480_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 19,
  'content_id': 0,
  'os': {'andyc': 53.0,
         'cwilms': 26.0,
         'czhao': 62.0,
         'ddenlinger': 63.0,
         'dteoh': 29.0,
         'jingxian@sranford.edu': 33.0,
         'kalvey': 37.0,
         'lfriedman@catflix.com': 31.0,
         'mariakaz': 39.0,
         'mrobbe': 19.0,
         'msemeniakin': 49.0,
         'mufford': 48.0,
         'rsharma': 62.0,
         'sdearaujo': 83.0,
         'sdu@catflix.com': 17.0,
         'ssharma': 22.0,
         'tgoodall@catflix.com': 61.0,
         'wwolcott': 75.0,
         'zchen': 48.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BarbieLife_B_fps23.97_720x480_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 20,
  'content_id': 1,
  'os': {'andrewp': 83.0,
         'andyc': 82.0,
         'czhao': 71.0,
         'ddenlinger': 77.0,
         'devenson@catflix.com': 74.0,
         'dteoh': 76.0,
         'jingxian@sranford.edu': 55.0,
         'kalvey': 100.0,
         'lfriedman@catflix.com': 89.0,
         'mangalap': 62.0,
         'mrobbe': 90.0,
         'msemeniakin': 56.0,
         'rbrodie': 95.0,
         'rgallardo': 94.0,
         'rsharma': 84.0,
         'svenkatrav@catflix.com': 64.0,
         'yjayaraman': 93.0,
         'zchen': 83.0,
         'zli': 50.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_1280x720_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 23,
  'content_id': 1,
  'os': {'aschuler': 72.0,
         'btorres': 84.0,
         'caleb': 97.0,
         'cwilms': 83.0,
         'decsobiel@gmail.com': 80.0,
         'hjagadeesan': 81.0,
         'kchen@catflix.com': 100.0,
         'mariakaz': 100.0,
         'mufford': 56.0,
         'rly': 79.0,
         'rwaters': 43.0,
         'sdearaujo': 88.0,
         'sdu@catflix.com': 92.0,
         'sfedorov@catflix.com': 97.0,
         'ssharma': 83.0,
         'tgoodall@catflix.com': 80.0,
         'thuang': 77.0,
         'timothy.l.robinson@comcast.net': 64.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_1920x1080_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 27,
  'content_id': 1,
  'os': {'aschuler': 6.0,
         'caleb': 4.0,
         'ddenlinger': 21.0,
         'devenson@catflix.com': 35.0,
         'hjagadeesan': 10.0,
         'jingxian@sranford.edu': 11.0,
         'kalvey': 1.0,
         'kchen@catflix.com': 11.0,
         'lfriedman@catflix.com': 16.0,
         'mangalap': 1.0,
         'rbrodie': 14.0,
         'rly': 32.0,
         'rwaters': 1.0,
         'sdearaujo': 17.0,
         'sdu@catflix.com': 3.0,
         'sfedorov@catflix.com': 8.0,
         'svenkatrav@catflix.com': 5.0,
         'tgoodall@catflix.com': 1.0,
         'timothy.l.robinson@comcast.net': 19.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_320x240_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 30,
  'content_id': 1,
  'os': {'andrewp': 8.0,
         'andyc': 28.0,
         'btorres': 1.0,
         'cwilms': 6.0,
         'czhao': 18.0,
         'decsobiel@gmail.com': 11.0,
         'dteoh': 1.0,
         'mariakaz': 9.0,
         'mrobbe': 13.0,
         'msemeniakin': 15.0,
         'mufford': 20.0,
         'rgallardo': 28.0,
         'rsharma': 9.0,
         'ssharma': 21.0,
         'thuang': 24.0,
         'yjayaraman': 26.0,
         'zchen': 14.0,
         'zli': 11.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_384x288_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 31,
  'content_id': 1,
  'os': {'aschuler': 25.0,
         'caleb': 68.0,
         'cwilms': 43.0,
         'ddenlinger': 51.0,
         'decsobiel@gmail.com': 37.0,
         'hjagadeesan': 67.0,
         'jingxian@sranford.edu': 32.0,
         'kalvey': 64.0,
         'kchen@catflix.com': 68.0,
         'mangalap': 46.0,
         'mariakaz': 76.0,
         'rgallardo': 72.0,
         'rly': 70.0,
         'rwaters': 37.0,
         'sdearaujo': 48.0,
         'sfedorov@catflix.com': 41.0,
         'ssharma': 54.0,
         'svenkatrav@catflix.com': 38.0,
         'tgoodall@catflix.com': 61.0,
         'yjayaraman': 74.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_512x384_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 32,
  'content_id': 1,
  'os': {'btorres': 18.0,
         'caleb': 68.0,
         'cwilms': 19.0,
         'dteoh': 33.0,
         'jingxian@sranford.edu': 22.0,
         'lfriedman@catflix.com': 15.0,
         'mariakaz': 46.0,
         'mrobbe': 26.0,
         'msemeniakin': 26.0,
         'mufford': 42.0,
         'rbrodie': 34.0,
         'rgallardo': 71.0,
         'rly': 61.0,
         'rwaters': 14.0,
         'sdearaujo': 51.0,
         'svenkatrav@catflix.com': 20.0,
         'timothy.l.robinson@comcast.net': 30.0,
         'zchen': 33.0,
         'zli': 41.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_512x384_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 33,
  'content_id': 1,
  'os': {'andrewp': 32.0,
         'andyc': 34.0,
         'aschuler': 23.0,
         'btorres': 27.0,
         'czhao': 29.0,
         'devenson@catflix.com': 39.0,
         'hjagadeesan': 28.0,
         'kalvey': 26.0,
         'kchen@catflix.com': 64.0,
         'lfriedman@catflix.com': 24.0,
         'mangalap': 48.0,
         'rbrodie': 14.0,
         'rsharma': 36.0,
         'sdu@catflix.com': 6.0,
         'sfedorov@catflix.com': 40.0,
         'svenkatrav@catflix.com': 14.0,
         'thuang': 11.0,
         'timothy.l.robinson@comcast.net': 60.0,
         'zli': 28.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_512x384_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 34,
  'content_id': 1,
  'os': {'andrewp': 49.0,
         'andyc': 50.0,
         'aschuler': 39.0,
         'caleb': 98.0,
         'ddenlinger': 49.0,
         'decsobiel@gmail.com': 66.0,
         'devenson@catflix.com': 71.0,
         'hjagadeesan': 68.0,
         'kchen@catflix.com': 57.0,
         'mrobbe': 59.0,
         'mufford': 55.0,
         'rbrodie': 98.0,
         'rwaters': 51.0,
         'sdu@catflix.com': 96.0,
         'thuang': 48.0,
         'timothy.l.robinson@comcast.net': 48.0,
         'zli': 63.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_720x480_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 35,
  'content_id': 1,
  'os': {'andrewp': 57.0,
         'btorres': 25.0,
         'czhao': 48.0,
         'decsobiel@gmail.com': 49.0,
         'devenson@catflix.com': 80.0,
         'dteoh': 67.0,
         'mangalap': 71.0,
         'msemeniakin': 81.0,
         'rgallardo': 83.0,
         'rly': 55.0,
         'rsharma': 72.0,
         'sfedorov@catflix.com': 77.0,
         'ssharma': 50.0,
         'tgoodall@catflix.com': 83.0,
         'thuang': 38.0,
         'yjayaraman': 55.0,
         'zchen': 49.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/BeautifulGirls_A_fps23.97_720x480_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 36,
  'content_id': 2,
  'os': {'andrewp': 83.0,
         'andyc': 94.0,
         'czhao': 91.0,
         'ddenlinger': 76.0,
         'devenson@catflix.com': 96.0,
         'dteoh': 85.0,
         'jingxian@sranford.edu': 63.0,
         'kalvey': 100.0,
         'lfriedman@catflix.com': 81.0,
         'mangalap': 49.0,
         'mrobbe': 93.0,
         'msemeniakin': 89.0,
         'rbrodie': 99.0,
         'rgallardo': 93.0,
         'rsharma': 92.0,
         'wwolcott': 73.0,
         'yjayaraman': 98.0,
         'zchen': 88.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_1280x720_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 39,
  'content_id': 2,
  'os': {'aprakash@catflix.com': 85.0,
         'aschuler': 72.0,
         'btorres': 91.0,
         'caleb': 52.0,
         'cwilms': 92.0,
         'decsobiel@gmail.com': 86.0,
         'hjagadeesan': 72.0,
         'kchen@catflix.com': 100.0,
         'mariakaz': 100.0,
         'mufford': 70.0,
         'rly': 90.0,
         'rwaters': 100.0,
         'sdearaujo': 85.0,
         'sdu@catflix.com': 98.0,
         'sfedorov@catflix.com': 98.0,
         'ssharma': 91.0,
         'thuang': 49.0,
         'timothy.l.robinson@comcast.net': 90.0,
         'vyelevich': 89.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_1920x1080_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 44,
  'content_id': 2,
  'os': {'aprakash@catflix.com': 41.0,
         'aschuler': 8.0,
         'caleb': 7.0,
         'ddenlinger': 21.0,
         'devenson@catflix.com': 18.0,
         'hjagadeesan': 5.0,
         'jingxian@sranford.edu': 1.0,
         'kalvey': 1.0,
         'kchen@catflix.com': 14.0,
         'lfriedman@catflix.com': 10.0,
         'mangalap': 1.0,
         'rbrodie': 2.0,
         'rly': 28.0,
         'rwaters': 1.0,
         'sdearaujo': 20.0,
         'sdu@catflix.com': 1.0,
         'sfedorov@catflix.com': 7.0,
         'timothy.l.robinson@comcast.net': 10.0,
         'wwolcott': 1.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_320x240_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 46,
  'content_id': 2,
  'os': {'andrewp': 19.0,
         'andyc': 24.0,
         'btorres': 13.0,
         'cwilms': 5.0,
         'czhao': 17.0,
         'decsobiel@gmail.com': 13.0,
         'dteoh': 1.0,
         'mariakaz': 39.0,
         'mrobbe': 3.0,
         'msemeniakin': 34.0,
         'mufford': 24.0,
         'rgallardo': 24.0,
         'rsharma': 38.0,
         'ssharma': 1.0,
         'thuang': 7.0,
         'vyelevich': 16.0,
         'yjayaraman': 15.0,
         'zchen': 12.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_384x288_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 47,
  'content_id': 2,
  'os': {'aprakash@catflix.com': 63.0,
         'aschuler': 21.0,
         'caleb': 68.0,
         'cwilms': 52.0,
         'ddenlinger': 47.0,
         'decsobiel@gmail.com': 41.0,
         'hjagadeesan': 63.0,
         'jingxian@sranford.edu': 28.0,
         'kalvey': 100.0,
         'kchen@catflix.com': 86.0,
         'mangalap': 55.0,
         'mariakaz': 73.0,
         'rgallardo': 82.0,
         'rly': 67.0,
         'rwaters': 40.0,
         'sdearaujo': 49.0,
         'sfedorov@catflix.com': 45.0,
         'ssharma': 47.0,
         'vyelevich': 42.0,
         'yjayaraman': 74.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_512x384_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 48,
  'content_id': 2,
  'os': {'btorres': 46.0,
         'caleb': 54.0,
         'cwilms': 35.0,
         'dteoh': 11.0,
         'jingxian@sranford.edu': 39.0,
         'lfriedman@catflix.com': 31.0,
         'mariakaz': 52.0,
         'mrobbe': 19.0,
         'msemeniakin': 54.0,
         'mufford': 64.0,
         'rbrodie': 14.0,
         'rgallardo': 74.0,
         'rly': 63.0,
         'rwaters': 43.0,
         'sdearaujo': 51.0,
         'timothy.l.robinson@comcast.net': 39.0,
         'vyelevich': 39.0,
         'zchen': 22.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_512x384_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 49,
  'content_id': 2,
  'os': {'andrewp': 22.0,
         'andyc': 27.0,
         'aprakash@catflix.com': 47.0,
         'aschuler': 3.0,
         'btorres': 20.0,
         'czhao': 52.0,
         'devenson@catflix.com': 33.0,
         'hjagadeesan': 40.0,
         'kalvey': 62.0,
         'kchen@catflix.com': 22.0,
         'lfriedman@catflix.com': 44.0,
         'mangalap': 19.0,
         'rbrodie': 15.0,
         'rsharma': 37.0,
         'sdu@catflix.com': 7.0,
         'sfedorov@catflix.com': 52.0,
         'thuang': 12.0,
         'timothy.l.robinson@comcast.net': 21.0,
         'wwolcott': 27.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_512x384_x264_nflx3pass_28rf_bitrate10000.yuv'},
 {'asset_id': 50,
  'content_id': 2,
  'os': {'andrewp': 62.0,
         'andyc': 79.0,
         'aschuler': 30.0,
         'caleb': 97.0,
         'ddenlinger': 49.0,
         'decsobiel@gmail.com': 43.0,
         'devenson@catflix.com': 69.0,
         'hjagadeesan': 58.0,
         'kchen@catflix.com': 69.0,
         'mrobbe': 58.0,
         'mufford': 85.0,
         'rbrodie': 74.0,
         'rwaters': 75.0,
         'sdu@catflix.com': 44.0,
         'thuang': 49.0,
         'timothy.l.robinson@comcast.net': 58.0,
         'vyelevich': 75.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_720x480_x264_nflx3pass_22rf_bitrate10000.yuv'},
 {'asset_id': 51,
  'content_id': 2,
  'os': {'andrewp': 47.0,
         'aprakash@catflix.com': 76.0,
         'btorres': 27.0,
         'czhao': 68.0,
         'decsobiel@gmail.com': 64.0,
         'devenson@catflix.com': 88.0,
         'dteoh': 48.0,
         'mangalap': 34.0,
         'msemeniakin': 83.0,
         'rgallardo': 90.0,
         'rly': 87.0,
         'rsharma': 69.0,
         'sfedorov@catflix.com': 66.0,
         'ssharma': 67.0,
         'thuang': 42.0,
         'wwolcott': 78.0,
         'yjayaraman': 71.0,
         'zchen': 47.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_720x480_x264_nflx3pass_25rf_bitrate10000.yuv'},
 {'asset_id': 52,
  'content_id': 2,
  'os': {'andyc': 46.0,
         'cwilms': 21.0,
         'czhao': 61.0,
         'ddenlinger': 36.0,
         'dteoh': 20.0,
         'jingxian@sranford.edu': 47.0,
         'kalvey': 80.0,
         'lfriedman@catflix.com': 55.0,
         'mariakaz': 48.0,
         'mrobbe': 29.0,
         'msemeniakin': 47.0,
         'mufford': 59.0,
         'rsharma': 77.0,
         'sdearaujo': 52.0,
         'sdu@catflix.com': 22.0,
         'ssharma': 40.0,
         'wwolcott': 68.0,
         'yjayaraman': 98.0,
         'zchen': 37.0},
  'path': '/mnt/hgfs/zli-nflx3/VMAF_Plus_study/dis_yuv/Bloodline_A_fps23.97_720x480_x264_nflx3pass_28rf_bitrate10000.yuv'},
]
