function [ pred_cell ] = populateX( length, X, size_m )
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
    pred_cell = cell(length, 1);
    for i = 1:length
        pred_cell{i, 1} = [eye(size_m), repmat(X(i,:), size_m, 1)];
    end
    return;
end

