import argparse
from src.config import load_config
from src.sorter import FileSorter

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='自动目录整理工具')
    parser.add_argument('directory', help='要整理的目录路径')
    parser.add_argument('-c', '--config', help='配置文件路径')
    args = parser.parse_args()
    
    try:
        # 加载配置
        config = load_config(args.config)
        
        # 创建排序器并执行
        sorter = FileSorter(config)
        sorter.sort_directory(args.directory)
        
        print("目录整理完成!")
    except Exception as e:
        print(f"错误: {e}")

if __name__ == '__main__':
    main() 