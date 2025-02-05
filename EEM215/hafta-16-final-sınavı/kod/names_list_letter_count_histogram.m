clear all; close all; clc;
isimler = ["ALİ", "nour", "cem", "derya", "patRICK", 
    "sefa", "can", "Serhat", "TaHa", "sude", 
    "patrick", "merT", "Deniz", "AHmeT", "mesut", 
    "melike", "zeynep", "melisa", "merve", "ayşe"];
harfSayilari = zeros(1,size(isimler,1)*size(isimler,2));
for i=1:size(isimler,1)
    for j=1:size(isimler,2)
        harfSayilari((i-1)*size(isimler,2)+j) = strlength(isimler(i,j));
    end
end

% Histogram verilerini hesapla
[counts, edges] = histcounts(harfSayilari);
%%
% Histogramı stem() ile çiz
figure; set(gcf, "Position", 1e3*[1.0522 0.2210 0.2808 0.1680])
stem(edges(1:end-1)+0.5, counts, 'filled', ...
    'k.', 'LineWidth', 1.5, 'MarkerSize', 10);
xlabel('Harf Sayısı', 'FontWeight', 'bold');
ylabel('İsim Sayısı', 'FontWeight', 'bold');
title('İsimlerdeki Harf Sayılarının Histogramı');
grid on; set(gca, 'gridlinestyle', '--');
set(gca, 'xtick', [2.8, 3:7, 7.2], 'ytick', 0:6);
xlim([2.8, 7.2]); ylim([0 6.2]);
set(gca, 'XTickLabel', {'','3','4','5','6','7',''});
set(gca,'position',[0.0912, 0.2056, 0.8966, 0.6818]);